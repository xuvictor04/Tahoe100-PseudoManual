---
symbol: "ELOC"
type: "gene"
col: 7817
ensembl_id: "ENSG00000154582"
name: "elongin C"
location: "8q21.11"
module: 212
arm: "+"
pooled_cpm: 74.02
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# ELOC

*elongin C* — 8q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (18 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.34× (z +11.6, q 2e-28, up in 48 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2D3]] (+0.60, fdr 1e-05), [[INTS4]] (+0.59, fdr 1e-05), [[ZNF565]] (+0.57, fdr 3e-05); moves opposite to [[FOXJ2]] (-0.54, fdr 5e-05), [[STXBP3]] (-0.48, fdr 1e-04), [[RNF146]] (-0.46, fdr 9e-05).
> It is in [[Module 212]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.34×** | +11.6 | 2e-28 | 48/49 (NCI-H1573, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.71×** | +10.1 | 2e-21 | 39/48 (COLO 205, NCI-H1573, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.86×** | +8.2 | 4e-14 | 41/49 (PANC-1, NCI-H1792, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.26×** | +8.2 | 4e-14 | 41/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.80×** | +7.8 | 9e-13 | 45/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.70×** | +7.0 | 2e-10 | 42/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.60×** | +6.0 | 1e-07 | 28/42 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.55×** | +5.8 | 4e-07 | 39/48 (LoVo, SW480, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +5.6 | 1e-06 | 40/48 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.56×** | +5.5 | 2e-06 | 32/45 (HOP62, PANC-1, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +5.0 | 3e-05 | 37/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.44×** | +4.9 | 5e-05 | 35/48 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.41×** | +4.5 | 3e-04 | 32/48 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.5 | 3e-04 | 34/47 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +4.2 | 0.001 | 30/48 (C32, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.003 | 31/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.008 | 27/48 (KATO III, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.014 | 28/48 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.0 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +11.1) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SW480 (line)]] | alt | 55.0 | 6 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.52× (z +10.7) | — |
| [[LoVo (line)]] | wt | 53.5 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.01× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 53.0 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.99× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 99.0 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +9.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.63× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 71.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H1573 (line)]] | alt | 65.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.12× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 77.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.96× (z +9.8) | — |
| [[C32 (line)]] | wt | 89.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +11.4) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[COLO 205 (line)]] | alt | 56.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +14.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.2× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 102 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.46× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 71.6 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.91× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 45.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[A498 (line)]] | wt | 137 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.0) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[CFPAC-1 (line)]] | alt | 84.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[HEC-1-A (line)]] | alt | 61.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.84× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 62.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.34× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 53.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.5) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[KATO III (line)]] | alt | 70.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.25× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 90.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.2) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[Panc 03.27 (line)]] | alt | 69.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.3) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[RKO (line)]] | wt | 150 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.11× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 99.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.65× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.7) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[A-172 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2D3]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 661 |
| [[INTS4]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ZNF565]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ECD]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CTR9]] | +0.55 | +0.63 / +0.40 | both halves | 4e-05 | pathway: Affinity selection of immunoglobulins; STRING 932 |
| [[GP6-AS1]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[LRRC23]] | +0.55 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[GNAI3]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MED26]] | +0.55 | +0.54 / +0.50 | both halves | 1e-05 | pathway: RSV-host interactions |
| [[TNFRSF10D]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SAP18]] | +0.51 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[COQ10B]] | +0.51 | +0.61 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXJ2]] | -0.54 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[STXBP3]] | -0.48 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[RNF146]] | -0.46 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[CPSF2]] | -0.46 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[RHNO1]] | -0.45 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[SMC6]] | -0.44 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[NHLRC2]] | -0.43 | -0.39 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.4, -25.7); signed map (-43.4, 10.3). **Vector** length 66.7, 17.6% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +11.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +8.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +2.0 | +8.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[Fumaric acid (drug)]] 0.5 µM |  | +1.2 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +1.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | -4.3 | +3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -3.8 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -3.4 | +3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -3.4 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | +3.9 |
|  | [[Erlotinib (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | elongin C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.11 — chr8:73,939,169-73,972,307 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SIII; previously TCEB1 |
| Gene groups (HGNC) | Elongin complex |
| Reactome | 46 pathways, smallest: Evasion by RSV of host interferon responses; Inactivation of CSF3 (G-CSF) signaling; Signaling by CSF3 (G-CSF) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15369](https://www.uniprot.org/uniprotkb/Q15369) (Elongin-C):

> Component of the Elongin complex, also known as SIII, a general transcription elongation factor that increases the RNA polymerase II transcription elongation past template-encoded arresting sites; subunit A is transcriptionally active and its transcription activity is strongly enhanced by binding to the dimeric complex of the SIII regulatory subunits B and C (Elongin BC complex). In embryonic stem cells, the elongin BC complex is recruited by EPOP to Polycomb group (PcG) target genes in order …

**Summary**, from NCBI Gene [6921](https://www.ncbi.nlm.nih.gov/gene/6921):

> This gene encodes the protein elongin C, which is a subunit of the transcription factor B (SIII) complex. The SIII complex is composed of elongins A/A2, B and C. It activates elongation by RNA polymerase II by suppressing transient pausing of the polymerase at many sites within transcription units. Elongin A functions as the transcriptionally active component of the SIII complex, whereas elongins B and C are regulatory subunits. Elongin A2 is specifically expressed in the testis, and capable of …

**Accessions** — [HGNC:11617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11617) · Entrez [6921](https://www.ncbi.nlm.nih.gov/gene/6921) · UniProt [Q15369](https://www.uniprot.org/uniprotkb/Q15369) · Ensembl [ENSG00000154582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154582)

## Data

Gene col 7817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7817); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7817]; `tensor/DDL_lfc|DDL_z.npy` [7817]; `embed/gene_vectors.npy` [7817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7817 or target_col == 7817). Every well: [[ELOC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELOC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
