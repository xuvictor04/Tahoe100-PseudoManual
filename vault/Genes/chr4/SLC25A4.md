---
symbol: "SLC25A4"
type: "gene"
col: 7560
ensembl_id: "ENSG00000151729"
name: "solute carrier family 25 member 4"
location: "4q35.1"
module: 24
arm: "+"
pooled_cpm: 23.43
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SLC25A4

*solute carrier family 25 member 4* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.06× (z +10.3, q 3e-22, up in 45 of 45 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.67× (z +5.3, q 1e-05, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.167× (z -6.9, q 4e-09, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 30 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC17]] (+0.71, fdr 1e-05), [[LAMTOR5]] (+0.68, fdr 2e-04), [[C19orf81]] (+0.67, fdr 1e-04); moves opposite to [[USP39]] (-0.68, fdr 3e-05), [[EIF3F]] (-0.65, fdr 4e-05), [[PAPOLA]] (-0.59, fdr 2e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **4.06×** | +10.3 | 3e-22 | 45/45 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.90×** | +10.0 | 3e-21 | 45/45 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.67×** | +6.9 | 7e-10 | 38/43 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.50×** | +6.7 | 2e-09 | 39/45 (HepG2/C3A, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +5.3 | 1e-05 | 35/46 (SW 900, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.73×** | +4.0 | 0.005 | 30/41 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.69×** | +3.8 | 0.010 | 25/40 (SK-MEL-2, SNU-423, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.67×** | +3.8 | 0.011 | 30/45 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.61×** | +3.5 | 0.027 | 23/45 (MIA PaCa-2, LS 180, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.59×** | +3.4 | 0.038 | 29/45 (CFPAC-1, J82, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.045 | 22/46 (A549, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.57×** | +3.2 | 0.068 | 24/45 (J82, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7560.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.167×** | -6.9 | 4e-09 | 38/44 (A-427, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.256×** | -5.2 | 4e-05 | 33/45 (LS 180, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.342×** | -4.1 | 0.007 | 31/45 (NCI-H460, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.615×** | -3.6 | 0.045 | 23/45 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.644× | -3.3 | 0.12 | 27/46 (H4, NCI-H2347, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 43.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.64× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.141× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0556× (z -8.6) |
| [[C-33 A (line)]] | alt | 39.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 22.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +10.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 19.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.56× (z +8.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 10.3× (z +10.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 34.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.87× (z +9.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 30.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0327× (z -9.8) |
| [[A549 (line)]] | wt | 11.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 7.12× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HepG2_C3A (line)]] | wt | 28.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.14× (z +8.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HOP62 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.60× (z +8.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HS-578T (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.65× (z +9.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[J82 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +8.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0689× (z -9.9) |
| [[A-172 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 24 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC17]] | +0.71 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.68 | +0.30 / +0.71 | both halves | 2e-04 |  |
| [[C19orf81]] | +0.67 | +0.33 / +0.73 | both halves | 1e-04 |  |
| [[IMP3]] | +0.67 | +0.39 / +0.75 | both halves | 6e-05 |  |
| [[LAGE3]] | +0.66 | +0.21 / +0.73 | both halves | 6e-04 |  |
| [[KRTCAP2]] | +0.65 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[TMEM191A-1]] | +0.65 | +0.27 / +0.67 | both halves | 3e-04 |  |
| [[C4orf48]] | +0.65 | +0.26 / +0.69 | both halves | 4e-04 |  |
| [[UQCR10]] ⚠ | +0.64 | +0.30 / +0.72 | both halves | 2e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; ⚠ in the vector space only through flagged drug-doses |
| [[CNNM4]] | +0.64 | +0.38 / +0.66 | both halves | 7e-05 |  |
| [[RPL36AL]] ⚠ | +0.64 | +0.38 / +0.67 | both halves | 6e-05 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.63 | +0.33 / +0.69 | both halves | 1e-04 |  |
| [[TCAF1]] | +0.63 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[CCDC85B]] | +0.63 | +0.26 / +0.68 | both halves | 4e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP39]] | -0.68 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[EIF3F]] | -0.65 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[PAPOLA]] | -0.59 | -0.29 / -0.66 | both halves | 2e-04 |  |
| [[NAA50]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[U2AF2]] | -0.59 | -0.25 / -0.67 | both halves | 4e-04 |  |
| [[ATL3]] | -0.59 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[EWSR1]] | -0.58 | -0.29 / -0.64 | both halves | 2e-04 |  |
| [[UBQLN1]] | -0.58 | -0.45 / -0.67 | both halves | 3e-05 |  |
| [[MAPKAPK5]] | -0.57 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[NUDT3]] | -0.57 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[LY6G5B]] | -0.57 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[ILF3]] | -0.57 | -0.24 / -0.64 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.3, -19.1); signed map (-30.7, 10.6). **Vector** length 86.6, 25.9% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.8 | +10.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +2.4 | +6.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.4 | +10.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.5 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.5 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -8.8 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -7.9 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 25 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:185,143,266-185,150,382 (+) |
| Ensembl biotype | protein_coding |
| Also known as | T1, AAC1; previously PEO3, PEO2, ANT1 |
| Gene groups (HGNC) | Solute carrier family 25 |
| Hallmark sets | PEROXISOME, UV_RESPONSE_UP, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 13 pathways, smallest: Vpr-mediated induction of apoptosis by mitochondrial outer membrane permeabilization; Mitochondrial Uncoupling; Transport of nucleosides and free purine and pyrimidine bases across the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [P12235](https://www.uniprot.org/uniprotkb/P12235) (ADP/ATP translocase 1):

> ADP:ATP antiporter that mediates import of ADP into the mitochondrial matrix for ATP synthesis, and export of ATP out to fuel the cell. Cycles between the cytoplasmic-open state (c-state) and the matrix-open state (m-state): operates by the alternating access mechanism with a single substrate-binding site intermittently exposed to either the cytosolic (c-state) or matrix (m-state) side of the inner mitochondrial membrane (By similarity). Substrate exchange across the membrane occurs …

**Summary**, from NCBI Gene [291](https://www.ncbi.nlm.nih.gov/gene/291):

> This gene is a member of the mitochondrial carrier subfamily of solute carrier protein genes. The product of this gene functions as a gated pore that translocates ADP from the cytoplasm into the mitochondrial matrix and ATP from the mitochondrial matrix into the cytoplasm. The protein forms a homodimer embedded in the inner mitochondria membrane. Mutations in this gene have been shown to result in autosomal dominant progressive external opthalmoplegia and familial hypertrophic cardiomyopathy. …

**Accessions** — [HGNC:10990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10990) · Entrez [291](https://www.ncbi.nlm.nih.gov/gene/291) · UniProt [P12235](https://www.uniprot.org/uniprotkb/P12235) · Ensembl [ENSG00000151729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151729)

## Data

Gene col 7560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7560); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7560]; `tensor/DDL_lfc|DDL_z.npy` [7560]; `embed/gene_vectors.npy` [7560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7560 or target_col == 7560). Every well: [[SLC25A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC25A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
