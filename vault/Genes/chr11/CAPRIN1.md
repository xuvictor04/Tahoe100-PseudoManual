---
symbol: "CAPRIN1"
type: "gene"
col: 5695
ensembl_id: "ENSG00000135387"
name: "cell cycle associated protein 1"
location: "11p13"
module: 25
arm: "+"
pooled_cpm: 148.64
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# CAPRIN1

*cell cycle associated protein 1* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.55× (z +6.8, q 7e-09, up in 30 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.39× (z +5.3, q 3e-05, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.633× (z -4.7, q 0.002, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NONO]] (+0.77, fdr 7e-06), [[IPO5]] (+0.74, fdr 7e-06), [[SF3B4]] (+0.73, fdr 7e-06); moves opposite to [[COMMD6]] (-0.72, fdr 1e-05), [[DCTN6-DT]] (-0.72, fdr 1e-05), [[C19orf81]] (-0.72, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +6.8 | 7e-09 | 30/44 (SNU-423, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +5.5 | 9e-06 | 41/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.3 | 3e-05 | 34/48 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.9 | 2e-04 | 33/49 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.6 | 5e-04 | 35/47 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.004 | 30/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.009 | 29/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.029 | 29/48 (LoVo, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.16× | +3.4 | 0.045 | 17/48 (LoVo, HT-29, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.050 | 24/48 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.050 | 24/48 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.057 | 32/48 (LOX-IMVI, KATO III, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.062 | 26/48 (HT-29, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.10 | 22/49 (HT-29, LS 180, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5695.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.633×** | -4.7 | 0.002 | 36/48 (HEC-1-A, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.763×** | -4.4 | 0.003 | 28/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.686×** | -3.9 | 0.021 | 38/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.797×** | -3.6 | 0.046 | 27/47 (NCI-H2030, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.805×** | -3.5 | 0.046 | 32/48 (J82, AsPC-1, …) | two highest doses |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.864× | -3.4 | 0.065 | 12/49 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.722×** | -3.4 | 0.065 | 26/49 (PANC-1, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.820×** | -3.2 | 0.084 | 21/48 (KATO III, A549, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 0.741× | -3.1 | 0.13 | 26/48 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 124 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 68.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.7) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[SNU-423 (line)]] | alt | 146 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +10.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 280 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.9) ⚠ cell-cycle shift, explains ~11% of this change |
| [[NCI-H23 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -8.8) ⚠ cell-cycle shift, explains ~2% of this change |
| [[A-172 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 233 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 178 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 159 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 95.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 154 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 120 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 115 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 150 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 175 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 245 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NONO]] | +0.77 | +0.70 / +0.81 | both halves | 7e-06 | STRING 483 |
| [[IPO5]] | +0.74 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[SF3B4]] | +0.73 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.73 | +0.54 / +0.78 | both halves | 1e-05 |  |
| [[BTBD1]] | +0.73 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[EIF4H]] | +0.73 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[MOB1A]] | +0.72 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[PSME3]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[TWF1]] | +0.72 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[UBQLN4]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[RCN1]] | +0.70 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[XRCC6]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD6]] | -0.72 | -0.54 / -0.78 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.72 | -0.53 / -0.77 | both halves | 1e-05 |  |
| [[C19orf81]] | -0.72 | -0.44 / -0.78 | both halves | 3e-05 |  |
| [[TMEM258]] | -0.72 | -0.59 / -0.75 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | -0.72 | -0.54 / -0.74 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | -0.70 | -0.47 / -0.76 | both halves | 2e-05 |  |
| [[ARID3A]] | -0.70 | -0.53 / -0.74 | both halves | 1e-05 |  |
| [[SNHG19]] | -0.70 | -0.50 / -0.74 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.69 | -0.54 / -0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | -0.69 | -0.52 / -0.75 | both halves | 1e-05 |  |
| [[AFMID]] | -0.69 | -0.51 / -0.73 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.68 | -0.57 / -0.71 | both halves | 9e-06 |  |
| [[CIAO2B]] | -0.67 | -0.46 / -0.71 | both halves | 2e-05 |  |
| [[GABARAPL2]] | -0.67 | -0.48 / -0.75 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.830). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.3, -23.2); signed map (-16.2, -37.8). **Vector** length 134, 44.2% of its response variance represented; |z| ≥ 3 in 779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.8 | +2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.5 | +4.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.9 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.6 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Erlotinib (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +1.0 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -5.5 | -4.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.8 | -3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.7 | -2.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.6 | -2.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cell cycle associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:34,051,731-34,102,610 (+) |
| Ensembl biotype | protein_coding |
| Also known as | caprin-1, RNG105; previously M11S1, GPIAP1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14444](https://www.uniprot.org/uniprotkb/Q14444) (Caprin-1):

> mRNA-binding protein that acts as a regulator of mRNAs transport, translation and/or stability, and which is involved in neurogenesis, synaptic plasticity in neurons and cell proliferation and migration in multiple cell types. Plays an essential role in cytoplasmic stress granule formation. Acts as an mRNA regulator by mediating formation of some phase-separated membraneless compartment: undergoes liquid-liquid phase separation upon binding to target mRNAs, leading to assemble mRNAs into …

**Summary**, from NCBI Gene [4076](https://www.ncbi.nlm.nih.gov/gene/4076):

> Enables several functions, including ATP binding activity; molecular condensate scaffold activity; and signaling adaptor activity. Involved in membraneless organelle assembly; positive regulation of stress granule assembly; and regulation of gene expression. Located in cell leading edge and cytosol. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6743) · Entrez [4076](https://www.ncbi.nlm.nih.gov/gene/4076) · UniProt [Q14444](https://www.uniprot.org/uniprotkb/Q14444) · Ensembl [ENSG00000135387](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135387)

## Data

Gene col 5695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5695); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5695]; `tensor/DDL_lfc|DDL_z.npy` [5695]; `embed/gene_vectors.npy` [5695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5695 or target_col == 5695). Every well: [[CAPRIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPRIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
