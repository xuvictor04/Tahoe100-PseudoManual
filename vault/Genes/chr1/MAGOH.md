---
symbol: "MAGOH"
type: "gene"
col: 8507
ensembl_id: "ENSG00000162385"
name: "mago homolog, exon junction complex subunit"
location: "1p32.3"
module: 210
arm: "+"
pooled_cpm: 33.62
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# MAGOH

*mago homolog, exon junction complex subunit* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (16 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.00× (z +12.6, q 2e-33, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.738× (z -7.8, q 5e-12, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSN]] (+0.67, fdr 1e-05), [[DDX49]] (+0.66, fdr 1e-05), [[RTF2]] (+0.62, fdr 3e-05); moves opposite to [[NBPF14]] (-0.47, fdr 2e-04), [[PEAK1]] (-0.45, fdr 5e-05), [[SOX4]] (-0.45, fdr 2e-04).
> It is in [[Module 210]], a single-armed module (tRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 20 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +12.6 | 2e-33 | 43/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.67×** | +9.3 | 6e-18 | 36/45 (NCI-H23, HOP62, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.66×** | +9.2 | 8e-18 | 41/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.61×** | +9.1 | 1e-17 | 38/48 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.56×** | +8.0 | 1e-13 | 40/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +7.5 | 7e-12 | 32/47 (NCI-H1573, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +7.4 | 2e-11 | 33/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +6.5 | 4e-09 | 26/48 (HS-578T, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.46×** | +6.3 | 1e-08 | 26/42 (SW480, NCI-H2030, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +6.0 | 9e-08 | 27/45 (HepG2/C3A, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.5 | 2e-06 | 26/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.34×** | +5.4 | 4e-06 | 28/48 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.36×** | +5.3 | 4e-06 | 21/38 (A549, NCI-H460, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.9 | 4e-05 | 24/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.30×** | +4.7 | 8e-05 | 21/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 2e-04 | 21/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.001 | 19/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.027 | 13/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.034 | 15/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.042 | 16/46 (H4, RPMI-7951, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.074 | 8/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8507.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.738×** | -7.8 | 5e-12 | 38/48 (A498, J82, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.706×** | -6.3 | 9e-08 | 27/48 (SW48, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Decitabine (drug)]] 5 µM |  | **0.759×** | -4.8 | 3e-04 | 26/47 (SW 1271, LOX-IMVI, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.818×** | -3.5 | 0.068 | 15/47 (A-427, LoVo, …) | rises with dose |  |
| [[Malotilate (drug)]] 5 µM |  | **0.831×** | -3.3 | 0.094 | 8/48 (SW48, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.842× | -3.1 | 0.18 | 10/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 37.5 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.49× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 23.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[A-427 (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[KATO III (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 31.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.45× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 46.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H661 (line)]] | alt | 47.3 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0833× (z -9.4) |
| [[A-172 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSN]] | +0.67 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[DDX49]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[RTF2]] | +0.62 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[FUBP3]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[NUP214]] | +0.61 | +0.53 / +0.68 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 541 |
| [[TMX2]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[NAA20]] | +0.60 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[BAG5]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[XPNPEP3]] | +0.58 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[CWF19L1]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[MFN2]] | +0.57 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[EARS2]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF14]] | -0.47 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[PEAK1]] | -0.45 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[SOX4]] | -0.45 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[ZNF706]] | -0.44 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[HYCC1]] | -0.44 | -0.35 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.7, -12.2); signed map (-32.5, -28.7). **Vector** length 66.6, 12.1% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.8 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +3.9 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +3.1 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +3.0 | +6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.7 | +9.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +6.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.2 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.8 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.6 | +3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.8 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | mago homolog, exon junction complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:53,226,900-53,238,518 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAGOHA, MAGOH1 |
| Gene groups (HGNC) | Exon junction complex; Spliceosomal P complex |
| Reactome | 13 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P61326](https://www.uniprot.org/uniprotkb/P61326) (Protein mago nashi homolog):

> Required for pre-mRNA splicing as component of the spliceosome. Plays a redundant role with MAGOHB as core component of the exon junction complex (EJC) and in the nonsense-mediated decay (NMD) pathway. The EJC is a dynamic structure consisting of core proteins and several peripheral nuclear and cytoplasmic associated factors that join the complex only transiently either during EJC assembly or during subsequent mRNA metabolism. The EJC marks the position of the exon-exon junction in the mature …

**Summary**, from NCBI Gene [4116](https://www.ncbi.nlm.nih.gov/gene/4116):

> Drosophila that have mutations in their mago nashi (grandchildless) gene produce progeny with defects in germplasm assembly and germline development. This gene encodes the mammalian mago nashi homolog. In mammals, mRNA expression is not limited to the germ plasm, but is expressed ubiquitously in adult tissues and can be induced by serum stimulation of quiescent fibroblasts. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6815](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6815) · Entrez [4116](https://www.ncbi.nlm.nih.gov/gene/4116) · UniProt [P61326](https://www.uniprot.org/uniprotkb/P61326) · Ensembl [ENSG00000162385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162385)

## Data

Gene col 8507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8507); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8507]; `tensor/DDL_lfc|DDL_z.npy` [8507]; `embed/gene_vectors.npy` [8507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8507 or target_col == 8507). Every well: [[MAGOH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGOH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
