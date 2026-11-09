---
symbol: "CNPY2"
type: "gene"
col: 15059
ensembl_id: "ENSG00000257727"
name: "canopy FGF signaling regulator 2"
location: "12q13.3"
module: 118
arm: "+"
pooled_cpm: 23.69
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# CNPY2

*canopy FGF signaling regulator 2* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +6.6, q 2e-08, up in 37 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 4.55×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.405× (z -8.8, q 7e-16, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APPBP2]] (+0.70, fdr 7e-06), [[NDUFS3]] (+0.69, fdr 1e-05), [[MED4]] (+0.64, fdr 2e-05); moves opposite to [[DIAPH1]] (-0.57, fdr 1e-05), [[NCOR2]] (-0.57, fdr 3e-05), [[ADAMTSL5]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15059.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 4.55×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.6 | 2e-08 | 37/47 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +6.3 | 1e-07 | 33/43 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +5.6 | 4e-06 | 21/34 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +5.3 | 2e-05 | 35/44 (SK-MEL-2, H4, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +3.9 | 0.013 | 23/38 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.6 | 0.036 | 4/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.4 | 0.050 | 21/45 (J82, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | 1.24× | +3.0 | 0.19 | 18/48 (SW 900, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15059.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.405×** | -8.8 | 7e-16 | 41/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.414×** | -8.6 | 2e-15 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.479×** | -7.2 | 1e-10 | 37/46 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.650×** | -5.9 | 4e-07 | 36/47 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.553×** | -5.8 | 9e-07 | 37/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.367×** | -5.1 | 3e-05 | 34/45 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.413×** | -4.5 | 5e-04 | 31/48 (NCI-H23, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.631×** | -4.5 | 5e-04 | 28/47 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.697×** | -3.5 | 0.027 | 22/48 (LS 180, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -3.2 | 0.067 | 20/47 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.719×** | -3.2 | 0.067 | 23/48 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.727×** | -3.1 | 0.088 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.719× | -3.0 | 0.10 | 19/48 (H4, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -8.7) |
| [[SW480 (line)]] | alt | 36.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.352× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.0) |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0965× (z -12.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -8.6) |
| [[KATO III (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 32.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.278× (z -9.2) |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APPBP2]] | +0.70 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[NDUFS3]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[MED4]] | +0.64 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[ZNF248]] | +0.63 | +0.34 / +0.68 | both halves | 1e-04 |  |
| [[ZNF785]] | +0.62 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[GOSR1]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[CNPY2-AS1]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SCNM1]] | +0.60 | +0.38 / +0.71 | both halves | 6e-05 |  |
| [[NGDN]] | +0.60 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[DNAJC30]] | +0.60 | +0.33 / +0.63 | both halves | 1e-04 |  |
| [[TVP23B]] | +0.60 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[SUPV3L1]] | +0.60 | +0.41 / +0.40 | both halves | 4e-05 |  |
| [[SYNRG]] | +0.59 | +0.44 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[NCOR2]] | -0.57 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ADAMTSL5]] | -0.57 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[R3HDM4]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ATP1A3]] | -0.56 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[EFR3A]] | -0.53 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[JUNB]] | -0.53 | -0.21 / -0.56 | both halves | 6e-04 |  |
| [[AFDN]] | -0.53 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[HPSE]] | -0.52 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[RAC1]] | -0.52 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[TMOD2]] | -0.52 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[H2AZ2]] | -0.51 | -0.21 / -0.51 | both halves | 7e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-52.6, 4.4); signed map (-5.2, -3.6). **Vector** length 63.5, 14.2% of its response variance represented; |z| ≥ 3 in 727 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.3 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | canopy FGF signaling regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,309,842-56,316,119 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HP10390, ZSIG9; previously TMEM4 |
| Gene groups (HGNC) | Canopy FGF signaling regulators; Saposin B type domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2B0](https://www.uniprot.org/uniprotkb/Q9Y2B0) (Protein canopy homolog 2):

> Positive regulator of neurite outgrowth by stabilizing myosin regulatory light chain (MRLC). It prevents MIR-mediated MRLC ubiquitination and its subsequent proteasomal degradation.

**Summary**, from NCBI Gene [10330](https://www.ncbi.nlm.nih.gov/gene/10330):

> Predicted to be active in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13529) · Entrez [10330](https://www.ncbi.nlm.nih.gov/gene/10330) · UniProt [Q9Y2B0](https://www.uniprot.org/uniprotkb/Q9Y2B0) · Ensembl [ENSG00000257727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257727)

## Data

Gene col 15059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15059); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15059]; `tensor/DDL_lfc|DDL_z.npy` [15059]; `embed/gene_vectors.npy` [15059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15059 or target_col == 15059). Every well: [[CNPY2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNPY2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
