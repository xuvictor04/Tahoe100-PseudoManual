---
symbol: "SLC2A1"
type: "gene"
col: 3900
ensembl_id: "ENSG00000117394"
name: "solute carrier family 2 member 1"
location: "1p34.2"
module: 99
arm: "+"
pooled_cpm: 233.11
n_lines_expressing: 46
n_dd_up: 7
n_dd_down: 32
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 9
direction_downstream: 14
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# SLC2A1

*solute carrier family 2 member 1* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.13× (z +14.5, q 3e-45, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.342× (z -23.3, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HK2]] (+0.71, fdr 7e-06), [[PGK1]] (+0.71, fdr 7e-06), [[NDRG1]] (+0.66, fdr 1e-05); moves opposite to [[N4BP2]] (-0.60, fdr 4e-05), [[UBXN2A]] (-0.59, fdr 3e-05), [[CPLANE1]] (-0.57, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[RIPK4]] → it (grade B ⚠); 14 go from it, the strongest it → [[NDRG1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.13×** | +14.5 | 3e-45 | 45/45 (A549, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.37×** | +6.9 | 1e-09 | 36/44 (HOP62, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.43×** | +5.3 | 2e-05 | 31/45 (NCI-H460, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.004 | 33/45 (AsPC-1, Panc 03.27, …) | top dose only | plate-row cell shift; position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.011 | 24/44 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.025 | 28/44 (A549, Hs 766T, …) | rises with dose | plate-row cell shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.3 | 0.073 | 19/44 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.49× | +3.2 | 0.10 | 21/44 (SHP-77, HepG2/C3A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Hesperidin (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.16 | 13/44 (AN3 CA, Panc 03.27, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3900.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.342×** | -23.3 | 0e+00 | 43/44 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.290×** | -19.0 | 0e+00 | 44/44 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.333×** | -16.3 | 0e+00 | 41/44 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.514×** | -14.5 | 1e-45 | 37/45 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.384×** | -14.1 | 2e-43 | 37/40 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.414×** | -13.0 | 7e-37 | 40/43 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.469×** | -11.7 | 2e-29 | 38/44 (SW480, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.473×** | -11.1 | 1e-26 | 41/43 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.510×** | -10.4 | 2e-23 | 40/45 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.529×** | -9.8 | 6e-21 | 33/44 (SW480, LS 180, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.551×** | -8.8 | 6e-17 | 38/44 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.585×** | -8.3 | 7e-15 | 42/44 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.624×** | -6.7 | 8e-10 | 30/41 (SW48, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.444×** | -6.5 | 3e-09 | 32/42 (A498, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.640×** | -6.5 | 3e-09 | 28/44 (SW48, A498, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.801×** | -4.9 | 4e-05 | 28/44 (SW480, SW1417, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.734×** | -4.8 | 5e-05 | 30/44 (KATO III, LS 180, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.736×** | -4.7 | 6e-05 | 28/44 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.741×** | -4.5 | 2e-04 | 27/45 (KATO III, Hs 766T, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.584×** | -4.3 | 4e-04 | 26/45 (SW480, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.826×** | -4.2 | 7e-04 | 23/44 (SW1417, SW480, …) | rises with dose | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.599×** | -4.1 | 9e-04 | 28/45 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 686 | 1 | 17 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 7.19× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -33.4) |
| [[SW48 (line)]] | wt | 930 | 0 | 15 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -24.2) |
| [[Panc 03.27 (line)]] | alt | 306 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -24.9) |
| [[KATO III (line)]] | alt | 448 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -21.6) |
| [[LOX-IMVI (line)]] | wt | 192 | 1 | 12 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.50× (z +10.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -22.9) |
| [[HT-29 (line)]] | alt | 666 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0945× (z -24.4) |
| [[NCI-H2347 (line)]] | alt | 312 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -32.1) |
| [[HEC-1-A (line)]] | alt | 168 | 1 | 10 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.42× (z +11.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -15.5) |
| [[LS 180 (line)]] | wt | 382 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -21.6) |
| [[SW 900 (line)]] | alt | 243 | 1 | 10 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.98× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -16.9) |
| [[SW1417 (line)]] | alt | 552 | 0 | 11 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -25.5) |
| [[AsPC-1 (line)]] | alt | 345 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 524 | 1 | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.76× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -14.0) |
| [[HCT15 (line)]] | alt | 313 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -22.8) |
| [[hTERT-HPNE (line)]] | wt | 189 | 1 | 7 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.92× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.266× (z -11.3) |
| [[A-172 (line)]] | wt | 129 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.153× (z -16.8) |
| [[A498 (line)]] | wt | 151 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -13.4) |
| [[Hs 766T (line)]] | wt | 312 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.45× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -24.9) |
| [[NCI-H1573 (line)]] | alt | 174 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 12.7× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.419× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 129 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.14× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -19.6) |
| [[COLO 205 (line)]] | alt | 337 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.7× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -19.1) |
| [[H4 (line)]] | wt | 347 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.1× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 117 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.95× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 160 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -20.2) |
| [[PANC-1 (line)]] | alt | 90.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -21.6) |
| [[RKO (line)]] | wt | 72.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -22.5) |
| [[A549 (line)]] | wt | 121 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 9.64× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -21.4) |
| [[HOP62 (line)]] | alt | 190 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.7× (z +11.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.350× (z -9.5) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.373× (z -8.7) |
| [[J82 (line)]] | alt | 122 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.84× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.339× (z -11.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.549× (z -9.3) |
| [[LoVo (line)]] | wt | 101 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.66× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.379× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 102 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.5× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 78.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.44× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -17.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 171 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.37× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.333× (z -9.1) |
| [[SNU-423 (line)]] | alt | 186 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -12.4) |
| [[BT-474 (line)]] | alt | 83.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -10.6) |
| [[C32 (line)]] | wt | 110 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.214× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 100 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 8.19× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -12.5) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -11.8) |
| [[HS-578T (line)]] | alt | 157 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 14.4× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 95.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.2× (z +12.0) | — |
| [[A-427 (line)]] | wt | 36.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 42.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 88.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 376 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HK2]] | +0.71 | +0.79 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 811 |
| [[PGK1]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 720 |
| [[NDRG1]] | +0.66 | +0.73 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 499 |
| [[INSIG2]] | +0.65 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[NXPH4]] | +0.65 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[SPNS2]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ALDOA]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 672 |
| [[ERO1A]] | +0.63 | +0.75 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[PKM]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives; STRING 814 |
| [[GPI]] | +0.62 | +0.70 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 554 |
| [[PFKFB3]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 767 |
| [[ANKRD37]] | +0.60 | +0.68 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP2]] | -0.60 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[UBXN2A]] | -0.59 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[CPLANE1]] | -0.57 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[EFCAB2]] | -0.52 | -0.65 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[GABPB1]] | -0.51 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[RNF115]] | -0.51 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[NDUFS1]] | -0.50 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[C11orf58]] | -0.50 | -0.56 / -0.23 | both halves | 5e-04 |  |
| [[ST7L]] | -0.49 | -0.59 / -0.25 | both halves | 4e-04 |  |
| [[CFLAR]] | -0.49 | -0.56 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[FAIM]] | -0.49 | -0.54 / -0.22 | both halves | 6e-04 |  |
| [[CARD8]] | -0.49 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[CCT6P3]] | -0.48 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[UPF3A]] | -0.47 | -0.57 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIPK4]] | B | RIPK4 activity raises SLC2A1's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 2.47× lower at baseline in the lines without RIPK4 | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[TOP2A]] | B | TOP2A activity raises SLC2A1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CA9]] | B | CA9 activity raises SLC2A1's level | lines that do not express CA9 (19) vs lines expressing it (31) | 2.01× lower at baseline in the lines without CA9 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[GPRC5A]] | B | GPRC5A activity raises SLC2A1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.29× lower at baseline in the lines without GPRC5A | 0.020 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[SPNS2]] | B | SPNS2 activity raises SLC2A1's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.13× lower at baseline in the lines without SPNS2 | 0.046 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[RAB20]] | B | RAB20 activity raises SLC2A1's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without RAB20 | 0.076 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[SPNS2]] | B | SPNS2 activity strengthens SLC2A1's drug response | lines that do not express SPNS2 (22) vs lines expressing it (23) | the lines without SPNS2 respond 0.79× as strongly (z diff +1.43); strongest at Idarubicin (hydrochloride) 5 µM: 0.62x vs 0.35x (z diff +2.6) | 0.097 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N; target measured in part of the lines; artifact flags |
| [[NDRG1]] | C | NDRG1 activity raises SLC2A1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 3.57× lower at baseline in the lines without NDRG1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1; co-absent with the target |
| [[SHB]] | C | SHB activity raises SLC2A1's level | lines that do not express SHB (5) vs lines expressing it (45) | 3.59× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | C | [[CIB1]], [[SEMA4B]], SLC2A1 activity raises NDRG1's level | lines that do not express CIB1, SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 8.44× lower at baseline in the lines without CIB1, SEMA4B, SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[SHB]] | C | [[SEMA4B]], SLC2A1 activity raises SHB's level | lines that do not express SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 4.14× lower at baseline in the lines without SEMA4B, SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[HK2]] | C | SLC2A1 activity raises HK2's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 2.14× lower at baseline in the lines without SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[ZBTB8A]] | C | SLC2A1 activity lowers ZBTB8A's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 1.59× higher at baseline in the lines without SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[UBXN2A]] | C | SLC2A1 activity lowers UBXN2A's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 1.54× higher at baseline in the lines without SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[SLC17A7]] | C | SLC2A1 activity lowers SLC17A7's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 1.50× higher at baseline in the lines without SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[RIPK4]] | C | [[SEMA4B]], SLC2A1 activity raises RIPK4's level | lines that do not express SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 5.50× lower at baseline in the lines without SEMA4B, SLC2A1 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent genes |
| [[SNX33]] | C | SLC2A1 activity raises SNX33's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 3.10× lower at baseline in the lines without SLC2A1 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent with the target |
| [[UBE2O]] | C | SLC2A1, [[TCAF2]] activity raises UBE2O's level | lines that do not express SLC2A1, TCAF2 (4) vs lines expressing them (46) | 1.67× lower at baseline in the lines without SLC2A1, TCAF2 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent genes |
| [[SLCO4A1]] | C | [[SEMA4B]], SLC2A1 activity raises SLCO4A1's level | lines that do not express SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 3.12× lower at baseline in the lines without SEMA4B, SLC2A1 | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent genes |
| [[PLOD2]] | C | SLC2A1 activity raises PLOD2's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 5.03× lower at baseline in the lines without SLC2A1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[FAIM]] | C | [[CIB1]], [[SEMA4B]], SLC2A1 activity lowers FAIM's level | lines that do not express CIB1, SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 1.66× higher at baseline in the lines without CIB1, SEMA4B, SLC2A1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, -15.3); signed map (-37.1, 28.4). **Vector** length 126, 46.4% of its response variance represented; |z| ≥ 3 in 1,503 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glycolysis* (reactome, mean cos +0.58 to 10); *Glucose metabolism* (reactome, mean cos +0.58 to 10); *glycolysis* (hallmark, mean cos +0.54 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +7.8 | -9.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +7.6 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.0 | -11.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.0 | +14.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.0 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | -1.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.9 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | -4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.3 | -16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -23.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.5 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -19.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -4.8 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.1 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.6 | -4.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.8 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | +0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 2 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:42,925,353-42,958,893 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DYT18, DYT9, GLUT-1; previously GLUT1, GLUT, HTLVR, CSE |
| Gene groups (HGNC) | Solute carrier family 2 |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, HEME_METABOLISM, HYPOXIA, ESTROGEN_RESPONSE_EARLY, MTORC1_SIGNALING |
| Reactome | 11 pathways, smallest: Vitamin C (ascorbate) metabolism; Cellular hexose transport; Regulation of insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [P11166](https://www.uniprot.org/uniprotkb/P11166) (Solute carrier family 2, facilitated glucose transporter member 1):

> Facilitative glucose transporter, which is responsible for constitutive or basal glucose uptake. Has a very broad substrate specificity; can transport a wide range of aldoses including both pentoses and hexoses. Most important energy carrier of the brain: present at the blood-brain barrier and assures the energy-independent, facilitative transport of glucose into the brain. In association with BSG and NXNL1, promotes retinal cone survival by increasing glucose uptake into photoreceptors (By …

**Summary**, from NCBI Gene [6513](https://www.ncbi.nlm.nih.gov/gene/6513):

> This gene encodes a major glucose transporter in the mammalian blood-brain barrier. The encoded protein is found primarily in the cell membrane and on the cell surface, where it can also function as a receptor for human T-cell leukemia virus (HTLV) I and II. Mutations in this gene have been found in a family with paroxysmal exertion-induced dyskinesia. [provided by RefSeq, Apr 2013]

**Accessions** — [HGNC:11005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11005) · Entrez [6513](https://www.ncbi.nlm.nih.gov/gene/6513) · UniProt [P11166](https://www.uniprot.org/uniprotkb/P11166) · Ensembl [ENSG00000117394](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117394)

## Data

Gene col 3900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3900); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3900]; `tensor/DDL_lfc|DDL_z.npy` [3900]; `embed/gene_vectors.npy` [3900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3900 or target_col == 3900). Every well: [[SLC2A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
