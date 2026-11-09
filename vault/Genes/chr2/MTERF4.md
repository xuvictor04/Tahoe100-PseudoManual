---
symbol: "MTERF4"
type: "gene"
col: 4320
ensembl_id: "ENSG00000122085"
name: "mitochondrial transcription termination factor 4"
location: "2q37.3"
module: 89
arm: "+"
pooled_cpm: 32.35
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# MTERF4

*mitochondrial transcription termination factor 4* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.35× (z +4.8, q 0.001, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.473× (z -10.7, q 3e-24, down in 27 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.746× (z -4.6, q 3e-04, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM4]] (+0.73, fdr 7e-06), [[ZNF721]] (+0.68, fdr 7e-06), [[ALKBH1]] (+0.68, fdr 1e-05); moves opposite to [[DPY19L1]] (-0.61, fdr 1e-05), [[ARL15]] (-0.56, fdr 5e-05), [[PEAK1]] (-0.56, fdr 1e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4320.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.8 | 0.001 | 29/48 (SW 900, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.009 | 20/47 (LoVo, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.22 | 15/48 (SW1417, A549, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.46× | +3.1 | 0.22 | 11/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.22 | 15/48 (CHP-212, RKO, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.23 | 12/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4320.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.473×** | -10.7 | 3e-24 | 27/36 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.477×** | -10.6 | 6e-24 | 39/46 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.554×** | -9.2 | 5e-18 | 38/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.560×** | -9.1 | 2e-17 | 35/46 (H4, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.636×** | -7.1 | 2e-10 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.658×** | -6.0 | 2e-07 | 26/47 (SNU-423, SW 1271, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.729×** | -4.9 | 6e-05 | 25/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.710×** | -4.9 | 6e-05 | 25/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.746×** | -4.6 | 3e-04 | 24/48 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -4.3 | 0.001 | 24/48 (AN3 CA, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.830×** | -4.1 | 0.002 | 19/48 (SW 1088, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -4.1 | 0.002 | 17/48 (A-172, SW480, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.718×** | -3.7 | 0.010 | 20/47 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.800×** | -3.5 | 0.020 | 21/48 (H4, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.802×** | -3.4 | 0.020 | 19/48 (SW480, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4320. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.3 | 0 | 7 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -12.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW480 (line)]] | alt | 43.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[PANC-1 (line)]] | alt | 34.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 2 (1 ⚠) | — | [[Orlistat (drug)]] 0.05 µM 0.287× (z -8.8) |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[H4 (line)]] | wt | 47.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0694× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[HOP62 (line)]] | alt | 39.0 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0933× (z -10.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 46.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0822× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[SK-MEL-2 (line)]] | alt | 25.3 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0932× (z -14.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 24.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 20.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.309× (z -9.0) |
| [[CHP-212 (line)]] | wt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0880× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[COLO 205 (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.216× (z -9.2) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0829× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[J82 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[LoVo (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LS 180 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[NCI-H1573 (line)]] | alt | 64.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[NCI-H23 (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0427× (z -24.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.306× (z -8.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4320), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM4]] | +0.73 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[ZNF721]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.68 | +0.76 / +0.56 | both halves | 1e-05 | STRING 454 |
| [[ZNF573]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ZNF383]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[THAP6]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[GOSR1]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ZNF2]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ZSCAN25]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[UTP23]] | +0.64 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[RBSN]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[LAMB2P1]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L1]] | -0.61 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ARL15]] | -0.56 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[PEAK1]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[SRPK2]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.3, 6.4); signed map (-12.4, -16.6). **Vector** length 86.4, 19.0% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.4 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +4.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +0.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +3.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.5 | -10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.1 | -6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.9 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -2.0 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.7 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial transcription termination factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,072,169-241,102,332 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC61716; previously MTERFD2 |
| Reactome | 4 pathways, smallest: rRNA modification in the mitochondrion; rRNA processing in the mitochondrion; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6M4](https://www.uniprot.org/uniprotkb/Q7Z6M4) (Transcription termination factor 4, mitochondrial):

> Regulator of mitochondrial ribosome biogenesis and translation. Binds to mitochondrial ribosomal RNAs 16S, 12S and 7S and targets NSUN4 RNA methyltransferase to the mitochondrial large ribosomal subunit (mt-LSU). Binds and stabilizes a premature conformation of the 16S mitochondrial rRNA (16S mt-rRNA) during mt-LSU biogenesis. Also sequesters interfacial regions of the 16S mt-rRNA, which may prevent premature ribosomal subunit joining. Together with NSUN4, exposes functionally important regions …

**Summary**, from NCBI Gene [130916](https://www.ncbi.nlm.nih.gov/gene/130916):

> Enables RNA folding chaperone; protein-RNA adaptor activity; and rRNA binding activity. Involved in mitochondrial large ribosomal subunit assembly and rRNA processing. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28785) · Entrez [130916](https://www.ncbi.nlm.nih.gov/gene/130916) · UniProt [Q7Z6M4](https://www.uniprot.org/uniprotkb/Q7Z6M4) · Ensembl [ENSG00000122085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122085)

## Data

Gene col 4320: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4320); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4320, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4320]; `tensor/DDL_lfc|DDL_z.npy` [4320]; `embed/gene_vectors.npy` [4320]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4320 or target_col == 4320). Every well: [[MTERF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTERF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
