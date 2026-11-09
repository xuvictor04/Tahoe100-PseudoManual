---
symbol: "LURAP1L-AS1"
type: "gene"
col: 14016
ensembl_id: "ENSG00000235448"
name: "LURAP1L antisense RNA 1"
location: "9p23"
module: 133
arm: "+"
pooled_cpm: 20.82
n_lines_expressing: 47
n_dd_up: 42
n_dd_down: 5
n_dd_up_clean: 34
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# LURAP1L-AS1

*LURAP1L antisense RNA 1* — 9p23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.14× (z +22.8, q 0e+00, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.573× (z -6.4, q 1e-07, down in 27 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYNE1]] (+0.73, fdr 7e-06), [[NIBAN1]] (+0.67, fdr 7e-06), [[PLAC8L1]] (+0.67, fdr 7e-06); moves opposite to [[SMARCD2]] (-0.59, fdr 3e-05), [[SDHA]] (-0.57, fdr 8e-05), [[FLYWCH2]] (-0.54, fdr 4e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.14×** | +22.8 | 0e+00 | 31/43 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.40×** | +19.2 | 0e+00 | 44/44 (SHP-77, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.54×** | +14.3 | 2e-44 | 36/42 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.11×** | +8.5 | 4e-15 | 34/44 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +7.7 | 1e-12 | 26/39 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +6.8 | 8e-10 | 18/30 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.82×** | +6.8 | 9e-10 | 24/43 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.80×** | +6.7 | 2e-09 | 24/44 (SHP-77, RKO, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +6.3 | 2e-08 | 30/44 (LOX-IMVI, SW 900, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.69×** | +5.7 | 7e-07 | 22/44 (SNU-423, SHP-77, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +5.7 | 8e-07 | 18/35 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM |  | **1.42×** | +5.6 | 8e-07 | 25/45 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.41×** | +5.5 | 2e-06 | 23/46 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.39×** | +5.3 | 6e-06 | 19/45 (LOX-IMVI, SHP-77, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.58×** | +5.2 | 9e-06 | 23/44 (RKO, SNU-423, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.0 | 2e-05 | 23/45 (J82, NCI-H2030, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.55×** | +4.9 | 3e-05 | 19/44 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +4.7 | 9e-05 | 23/43 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 3e-04 | 18/43 (LOX-IMVI, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 7e-04 | 15/45 (RKO, HEC-1-A, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.44×** | +4.1 | 1e-03 | 18/44 (RKO, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14016.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.573×** | -6.4 | 1e-07 | 27/44 (A-427, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.583×** | -6.2 | 2e-07 | 25/44 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.567×** | -5.7 | 2e-06 | 25/44 (COLO 205, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -4.5 | 8e-04 | 22/42 (SW48, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.658×** | -4.2 | 0.003 | 18/43 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.734× | -3.1 | 0.16 | 10/44 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 58.7 | 6 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +21.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.243× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 40.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +18.1) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 14.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.2× (z +20.8) | — |
| [[A-427 (line)]] | wt | 25.5 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.161× (z -11.3) |
| [[J82 (line)]] | alt | 53.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +20.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +22.8) | — |
| [[SW48 (line)]] | wt | 40.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +10.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0570× (z -13.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[COLO 205 (line)]] | alt | 42.2 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.137× (z -9.5) |
| [[HOP62 (line)]] | alt | 14.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +17.0) | — |
| [[HS-578T (line)]] | alt | 10.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +13.4) | — |
| [[RKO (line)]] | wt | 55.4 | 1 | 2 (1 ⚠) | [[Artesunate (drug)]] 5 µM 3.96× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.138× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 27.3 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 15.3× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 52.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +12.8) | — |
| [[A498 (line)]] | wt | 8.21 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +12.4) | — |
| [[C32 (line)]] | wt | 15.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 13.3× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 11.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.8× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 30.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.33× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.142× (z -11.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 17.7 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.09× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.164× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 20.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +20.1) | — |
| [[NCI-H2030 (line)]] | alt | 10.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 12.9× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 72.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +17.3) | — |
| [[SW 900 (line)]] | alt | 23.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 12.0× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +14.5) | — |
| [[KATO III (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 8.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.48× (z +12.7) | — |
| [[NCI-H23 (line)]] | alt | 7.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +13.9) | — |
| [[SHP-77 (line)]] | alt | 20.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 16.5× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 21.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.69× (z +8.5) | — |
| [[SW480 (line)]] | alt | 12.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.5× (z +12.8) | — |
| [[A549 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 66.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNE1]] | +0.73 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[NIBAN1]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[RNF103-CHMP3]] | +0.66 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[LINC00571]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[CLIP1]] | +0.64 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[COP1-DT]] | +0.64 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[SLC3A2]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[LY96]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[LRIF1]] | +0.62 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[PRECSIT]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[EIF5]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCD2]] | -0.59 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[SDHA]] | -0.57 | -0.69 / -0.37 | both halves | 8e-05 |  |
| [[FLYWCH2]] | -0.54 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[NHP2]] | -0.53 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[BRAT1]] | -0.53 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[MMS19]] | -0.52 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[RPA1]] | -0.52 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[FAM102B]] | -0.52 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[PXMP4]] | -0.52 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[MED14]] | -0.52 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[MINK1]] | -0.52 | -0.54 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises LURAP1L-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | LURAP1L-AS1 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express LURAP1L-AS1 (3) vs lines expressing it (45) | the lines without LURAP1L-AS1: 0.74× the cells of the other lines | 0.025 | ⚠ few lines (3 vs 47); across organs; also absent: ELF4, FCHSD1; maybe low, not absent |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | LURAP1L-AS1 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express LURAP1L-AS1 (3) vs lines expressing it (45) | the lines without LURAP1L-AS1: 0.72× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: ELF4, FCHSD1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.2, 13.1); signed map (24.6, 3.8). **Vector** length 125, 34.1% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.8 | +19.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +22.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +14.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.6 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +7.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.1 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +5.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.7 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.8 | -6.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.3 | -4.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | LURAP1L antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9p23 — chr9:12,698,554-12,814,377 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49761) · Entrez [101929467](https://www.ncbi.nlm.nih.gov/gene/101929467) · Ensembl [ENSG00000235448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235448)

## Data

Gene col 14016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14016); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14016]; `tensor/DDL_lfc|DDL_z.npy` [14016]; `embed/gene_vectors.npy` [14016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14016 or target_col == 14016). Every well: [[LURAP1L-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LURAP1L-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
