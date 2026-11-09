---
symbol: "LANCL2"
type: "gene"
col: 5320
ensembl_id: "ENSG00000132434"
name: "LanC like glutathione S-transferase 2"
location: "7p11.2"
module: 51
arm: "+"
pooled_cpm: 56.8
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# LANCL2

*LanC like glutathione S-transferase 2* — 7p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +5.8, q 5e-06, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.206× (z -23.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WARS2]] (+0.78, fdr 7e-06), [[TRMO]] (+0.77, fdr 7e-06), [[DNAJB12]] (+0.74, fdr 1e-05); moves opposite to [[TMEM185A]] (-0.61, fdr 1e-05), [[SERAC1]] (-0.61, fdr 4e-05), [[STX7]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5320.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.8 | 5e-06 | 28/48 (BT-474, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +5.6 | 6e-06 | 28/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +4.3 | 0.003 | 25/48 (KATO III, H4, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.006 | 20/48 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.006 | 23/48 (A-427, A498, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.65×** | +3.9 | 0.008 | 23/48 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +3.9 | 0.009 | 22/48 (AsPC-1, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.013 | 23/47 (SW 900, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.063 | 11/48 (A-172, A549, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.063 | 13/48 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.096 | 20/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5320.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.206×** | -23.7 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.259×** | -20.3 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.325×** | -16.9 | 0e+00 | 48/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.326×** | -16.8 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.355×** | -15.5 | 0e+00 | 44/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.596×** | -10.6 | 2e-24 | 48/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.363×** | -7.9 | 2e-13 | 45/49 (NCI-H1573, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.596×** | -7.7 | 7e-13 | 40/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -6.4 | 1e-08 | 32/47 (NCI-H23, J82, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.678×** | -5.8 | 4e-07 | 28/47 (SW48, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.682×** | -5.5 | 2e-06 | 31/48 (RKO, SNU-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.710×** | -5.1 | 1e-05 | 34/48 (SW48, RKO, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.762×** | -3.9 | 0.004 | 21/48 (SW48, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.789×** | -3.5 | 0.016 | 18/48 (SNU-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.798×** | -3.2 | 0.046 | 19/44 (NCI-H1573, KATO III, …) | rises with dose | composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.050 | 16/48 (NCI-H1792, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5320. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 90.2 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.150× (z -23.5) |
| [[KATO III (line)]] | alt | 59.6 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.0) | [[Belinostat (drug)]] 5 µM 0.187× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 499 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0400× (z -35.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.130× (z -23.2) |
| [[NCI-H2030 (line)]] | alt | 41.2 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.248× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 65.9 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.168× (z -15.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.206× (z -14.2) |
| [[PANC-1 (line)]] | alt | 60.8 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.198× (z -16.8) |
| [[A-427 (line)]] | wt | 57.9 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.217× (z -14.6) |
| [[COLO 205 (line)]] | alt | 43.8 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.144× (z -13.3) |
| [[H4 (line)]] | wt | 87.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -14.1) |
| [[HT-29 (line)]] | alt | 38.8 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.203× (z -13.0) |
| [[LoVo (line)]] | wt | 59.3 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.176× (z -16.8) |
| [[LOX-IMVI (line)]] | wt | 51.0 | 1 | 4 | [[TAK-901 (drug)]] 0.05 µM 3.04× (z +9.9) | [[Belinostat (drug)]] 5 µM 0.205× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 63.1 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.127× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 29.6 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.215× (z -13.4) |
| [[RPMI-7951 (line)]] | alt | 59.2 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.162× (z -15.2) |
| [[SW48 (line)]] | wt | 72.4 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.178× (z -12.7) |
| [[HOP62 (line)]] | alt | 27.5 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.159× (z -13.4) |
| [[J82 (line)]] | alt | 25.8 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.220× (z -10.7) |
| [[LS 180 (line)]] | wt | 45.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 31.8 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.205× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 18.8 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.178× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 44.2 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.190× (z -12.7) |
| [[RKO (line)]] | wt | 32.7 | 0 | 4 | — | [[Belinostat (drug)]] 0.5 µM 0.155× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 57.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -10.7) |
| [[SNU-1 (line)]] | wt | 86.8 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.184× (z -14.1) |
| [[SNU-423 (line)]] | alt | 39.8 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.196× (z -11.9) |
| [[SW 900 (line)]] | alt | 50.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -17.7) |
| [[A-172 (line)]] | wt | 28.6 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.230× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 35.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.212× (z -11.3) |
| [[BT-474 (line)]] | alt | 81.3 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -15.8) |
| [[C-33 A (line)]] | alt | 52.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -13.7) |
| [[A549 (line)]] | wt | 33.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.230× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 25.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.200× (z -12.3) |
| [[HCT15 (line)]] | alt | 42.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.154× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 47.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -11.4) |
| [[A498 (line)]] | wt | 31.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.05 µM 0.328× (z -8.8) |
| [[C32 (line)]] | wt | 37.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.207× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 30.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.101× (z -13.4) |
| [[HS-578T (line)]] | alt | 25.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -8.7) |
| [[SHP-77 (line)]] | alt | 50.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.301× (z -9.6) |
| [[SW1417 (line)]] | alt | 24.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.304× (z -8.8) |
| [[AN3 CA (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5320), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2]] | +0.78 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[TRMO]] | +0.77 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[DNAJB12]] | +0.74 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[EPC2]] | +0.73 | +0.85 / +0.57 | both halves | 8e-06 |  |
| [[COQ7]] | +0.73 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.72 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[INO80]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[NSUN3]] | +0.71 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[RCBTB2]] | +0.71 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[AP5S1]] | +0.71 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[CDK12]] | +0.71 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[MRPS7]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185A]] | -0.61 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[SERAC1]] | -0.61 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[STX7]] | -0.59 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[STRN]] | -0.59 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[PCMT1]] | -0.58 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[MAST3]] | -0.58 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[NBPF3]] | -0.56 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[PCTP]] | -0.56 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[GMCL1]] | -0.56 | -0.57 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.4, 11.4); signed map (12.2, -30.2). **Vector** length 134, 42.4% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.5 | +2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +5.1 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.8 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +1.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -10.4 | -15.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -10.1 | -16.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -10.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.5 | -23.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -7.1 | -7.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.8 | -5.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -3.4 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | LanC like glutathione S-transferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p11.2 — chr7:55,365,337-55,433,737 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TASP; previously GPR69B |
| Gene groups (HGNC) | LanC like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS86](https://www.uniprot.org/uniprotkb/Q9NS86) (LanC-like protein 2):

> Necessary for abscisic acid (ABA) binding on the cell membrane and activation of the ABA signaling pathway in granulocytes.

**Summary**, from NCBI Gene [55915](https://www.ncbi.nlm.nih.gov/gene/55915):

> Enables phosphatidylinositol-3-phosphate binding activity; phosphatidylinositol-4-phosphate binding activity; and phosphatidylinositol-5-phosphate binding activity. Involved in negative regulation of DNA-templated transcription and positive regulation of abscisic acid-activated signaling pathway. Located in several cellular components, including cortical actin cytoskeleton; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6509) · Entrez [55915](https://www.ncbi.nlm.nih.gov/gene/55915) · UniProt [Q9NS86](https://www.uniprot.org/uniprotkb/Q9NS86) · Ensembl [ENSG00000132434](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132434)

## Data

Gene col 5320: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5320); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5320, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5320]; `tensor/DDL_lfc|DDL_z.npy` [5320]; `embed/gene_vectors.npy` [5320]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5320 or target_col == 5320). Every well: [[LANCL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LANCL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
