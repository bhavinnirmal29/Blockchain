from django.shortcuts import render, redirect
from .forms import BlockForm
from .models import Block, Blockchain
import hashlib


def calculate_hash(index, timestamp, data, previous_hash):
    """
    Calculate the hash value for a block based on its attributes.
    """
    sha = hashlib.sha256()
    sha.update(str(index).encode('utf-8') +
               str(timestamp).encode('utf-8') +
               str(data).encode('utf-8') +
               str(previous_hash).encode('utf-8'))
    return sha.hexdigest()


def blockchain_view(request):
    blockchain, _ = Blockchain.objects.get_or_create(name='My Blockchain')
    blocks = blockchain.blocks.order_by('index')

    if request.method == 'POST':
        form = BlockForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            previous_block = blocks.last() if blocks else None
            previous_hash = previous_block.hash if previous_block else ''

            new_block = Block(
                index=len(blocks) + 1,
                data=data,
                previous_hash=previous_hash
            )

            # Calculate the hash for the new block
            new_block.hash = calculate_hash(
                new_block.index,
                new_block.timestamp,
                new_block.data,
                new_block.previous_hash
            )

            new_block.save()
            blockchain.blocks.add(new_block)
            blockchain.save()
            return redirect('blockchain')
    else:
        form = BlockForm()

    return render(request, 'blockchain.html', {'blocks': blocks, 'form': form})


