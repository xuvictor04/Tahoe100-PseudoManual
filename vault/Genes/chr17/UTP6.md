---
symbol: "UTP6"
type: "gene"
col: 2981
ensembl_id: "ENSG00000108651"
name: "UTP6 small subunit processome component"
location: "17q11.2"
module: 49
arm: "+"
pooled_cpm: 80.78
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# UTP6

*UTP6 small subunit processome component* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.68× (z +16.5, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.783× (z -5.8, q 4e-06, down in 29 of 49 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNL2]] (+0.72, fdr 7e-06), [[NAT9]] (+0.69, fdr 5e-05), [[PRPF3]] (+0.69, fdr 7e-06); moves opposite to [[KANSL1L]] (-0.52, fdr 4e-04), [[RDH5]] (-0.52, fdr 3e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.68×** | +16.5 | 0e+00 | 48/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.45×** | +13.0 | 5e-36 | 45/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +9.4 | 1e-18 | 38/48 (HT-29, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.73×** | +9.1 | 2e-17 | 43/48 (SW480, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.63×** | +8.1 | 8e-14 | 41/48 (SNU-423, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +7.4 | 2e-11 | 31/48 (NCI-H1792, HT-29, …) | two highest doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.49×** | +6.6 | 3e-09 | 35/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +6.4 | 1e-08 | 33/47 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.35×** | +5.0 | 4e-05 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.0 | 0.003 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +4.0 | 0.003 | 27/48 (NCI-H23, NCI-H1792, …) | rises with dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.008 | 24/48 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.24×** | +3.5 | 0.022 | 21/47 (HT-29, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.22×** | +3.3 | 0.040 | 22/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.1 | 0.074 | 21/48 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Trimetrexate (drug)]] 5 µM |  | 1.14× | +3.0 | 0.090 | 8/49 (A498, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2981.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -5.8 | 4e-06 | 29/49 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.784×** | -4.1 | 0.014 | 30/48 (HCT15, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.782×** | -3.9 | 0.015 | 26/47 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.787×** | -3.7 | 0.028 | 23/45 (RPMI-7951, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.804×** | -3.7 | 0.028 | 23/47 (A549, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.806×** | -3.6 | 0.028 | 23/48 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -3.3 | 0.076 | 14/48 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -3.3 | 0.079 | 13/48 (A-427, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.827× | -3.1 | 0.13 | 20/48 (A549, NCI-H2030, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 133 | 6 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.80× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 68.7 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +12.8) | — |
| [[RKO (line)]] | wt | 71.5 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.9× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -12.5) |
| [[A-427 (line)]] | wt | 88.1 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.57× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 68.0 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 9.49× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 85.2 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.13× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 60.4 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.80× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 88.3 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.88× (z +9.9) | — |
| [[SW480 (line)]] | alt | 70.2 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.48× (z +15.1) | — |
| [[A549 (line)]] | wt | 108 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 8.93× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -8.7) |
| [[BT-474 (line)]] | alt | 60.2 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 9.45× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 55.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 49.2× (z +14.7) | — |
| [[HOP62 (line)]] | alt | 71.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.60× (z +11.9) | — |
| [[KATO III (line)]] | alt | 66.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.04× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 41.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 56.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.40× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 57.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 82.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.84× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 82.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.50× (z +10.1) | — |
| [[A498 (line)]] | wt | 209 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 92.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.80× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 55.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.95× (z +9.4) | — |
| [[C32 (line)]] | wt | 44.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 51.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.66× (z +10.1) | — |
| [[CHP-212 (line)]] | wt | 70.4 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0676× (z -12.6) |
| [[H4 (line)]] | wt | 85.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -8.7) |
| [[Hs 766T (line)]] | wt | 48.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.8× (z +9.3) | — |
| [[LoVo (line)]] | wt | 57.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.77× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 69.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.92× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 49.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 83.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.14× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -10.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 89.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.85× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 57.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.4× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 52.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.64× (z +8.6) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 116 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL2]] | +0.72 | +0.76 / +0.61 | both halves | 7e-06 | STRING 931 |
| [[NAT9]] | +0.69 | +0.75 / +0.39 | both halves | 5e-05 |  |
| [[PRPF3]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[MSTO2P]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[RARS1]] | +0.66 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[GAR1]] | +0.66 | +0.73 / +0.60 | both halves | 7e-06 | pathway: rRNA modification in the nucleus and cytosol |
| [[GNL3]] | +0.66 | +0.69 / +0.56 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 743 |
| [[AQR]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ZMYM6]] | +0.63 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[DIS3]] | +0.63 | +0.71 / +0.37 | both halves | 8e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 540 |
| [[PDIA5]] | +0.63 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[SCFD2]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANSL1L]] | -0.52 | -0.48 / -0.24 | both halves | 4e-04 |  |
| [[RDH5]] | -0.52 | -0.45 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.5, -32.5); signed map (-49.0, 6.5). **Vector** length 103, 31.0% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.4 | +9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.3 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +13.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.9 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +16.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.6 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.8 | +5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -5.8 | +3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | UTP6 small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:31,860,904-31,901,708 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCA66; previously C17orf40 |
| Gene groups (HGNC) | UTPb subcomplex |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYH9](https://www.uniprot.org/uniprotkb/Q9NYH9) (U3 small nucleolar RNA-associated protein 6 homolog):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Involved in nucleolar processing of pre-18S ribosomal RNA.

**Summary**, from NCBI Gene [55813](https://www.ncbi.nlm.nih.gov/gene/55813):

> Predicted to enable snoRNA binding activity. Involved in ribosomal small subunit biogenesis. Located in chromosome and nucleolus. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18279](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18279) · Entrez [55813](https://www.ncbi.nlm.nih.gov/gene/55813) · UniProt [Q9NYH9](https://www.uniprot.org/uniprotkb/Q9NYH9) · Ensembl [ENSG00000108651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108651)

## Data

Gene col 2981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2981); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2981]; `tensor/DDL_lfc|DDL_z.npy` [2981]; `embed/gene_vectors.npy` [2981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2981 or target_col == 2981). Every well: [[UTP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
