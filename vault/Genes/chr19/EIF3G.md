---
symbol: "EIF3G"
type: "gene"
col: 5131
ensembl_id: "ENSG00000130811"
name: "eukaryotic translation initiation factor 3 subunit G"
location: "19p13.2"
module: 7
arm: "+"
pooled_cpm: 30.89
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# EIF3G

*eukaryotic translation initiation factor 3 subunit G* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.99× (z +11.1, q 6e-26, up in 44 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.85× (z +6.2, q 9e-08, up in 40 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD6]] (+0.60, fdr 1e-05), [[GFER]] (+0.60, fdr 2e-05), [[AUP1]] (+0.57, fdr 3e-05); moves opposite to [[GGH]] (-0.50, fdr 3e-05), [[IGFBP2]] (-0.47, fdr 1e-04), [[C21orf58]] (-0.46, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5131.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.99×** | +11.1 | 6e-26 | 44/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.48×** | +8.9 | 2e-16 | 36/38 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +6.2 | 9e-08 | 40/47 (LoVo, H4, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +6.1 | 2e-07 | 41/48 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.87×** | +5.9 | 5e-07 | 33/41 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +5.7 | 1e-06 | 11/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +5.7 | 1e-06 | 41/47 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +5.4 | 4e-06 | 42/48 (PANC-1, J82, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.64×** | +5.0 | 3e-05 | 37/46 (BT-474, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.63×** | +4.7 | 1e-04 | 35/48 (COLO 205, LoVo, …) | two highest doses | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +4.6 | 2e-04 | 35/48 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +4.5 | 3e-04 | 27/47 (LoVo, LS 180, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +4.5 | 4e-04 | 35/47 (BT-474, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.51×** | +4.0 | 0.002 | 26/47 (A549, PANC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +3.8 | 0.005 | 28/48 (LS 180, PANC-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.006 | 28/48 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 25.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 24.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-423 (line)]] | alt | 36.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 30.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 32.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 31.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[GFER]] | +0.60 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[AUP1]] | +0.57 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[GTF2F1]] | +0.57 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[LRRC47]] | +0.55 | +0.64 / +0.45 | both halves | 3e-05 | STRING 450 |
| [[DCTN2]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[FLII]] | +0.55 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[SBDSP1-1]] | +0.54 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[SF3A1]] | +0.53 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[BOD1]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ACTR8]] | +0.52 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[EEF2]] | +0.52 | +0.54 / +0.47 | both halves | 2e-05 | STRING 644 |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGH]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[IGFBP2]] | -0.47 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[C21orf58]] | -0.46 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[ATP1B3]] | -0.46 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[RAD54L]] | -0.45 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[THSD4-AS1]] | -0.44 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[SAMD1]] | -0.44 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[NMU]] | -0.44 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[ASF1B]] | -0.44 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[CDC7]] | -0.44 | -0.40 / -0.40 | both halves | 4e-05 |  |
| [[DUT]] | -0.43 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[SPC25]] | -0.43 | -0.46 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.379). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.3, -2.3); signed map (-0.4, -11.0). **Vector** length 55.4, 11.8% of its response variance represented; |z| ≥ 3 in 663 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.9 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.8 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +3.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.9 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.6 | +1.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | -1.9 | +3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +1.4 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.4 | -2.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.1 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,115,014-10,119,918 (-) |
| Ensembl biotype | protein_coding |
| Also known as | eIF3-delta, eIF3-p44; previously EIF3S4 |
| Gene groups (HGNC) | RNA binding motif containing; Eukaryotic translation initiation factor 3 complex subunits |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75821](https://www.uniprot.org/uniprotkb/O75821) (Eukaryotic translation initiation factor 3 subunit G):

> RNA-binding component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for …

**Summary**, from NCBI Gene [8666](https://www.ncbi.nlm.nih.gov/gene/8666):

> This gene encodes a core subunit of the eukaryotic translation initiation factor 3 (eIF3) complex, which is required for initiation of protein translation. An N-terminal caspase cleavage product of the encoded protein may stimulate degradation of DNA. A mutation in this gene is associated with narcolepsy. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:3274](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3274) · Entrez [8666](https://www.ncbi.nlm.nih.gov/gene/8666) · UniProt [O75821](https://www.uniprot.org/uniprotkb/O75821) · Ensembl [ENSG00000130811](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130811)

## Data

Gene col 5131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5131); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5131]; `tensor/DDL_lfc|DDL_z.npy` [5131]; `embed/gene_vectors.npy` [5131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5131 or target_col == 5131). Every well: [[EIF3G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
