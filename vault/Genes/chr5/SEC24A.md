---
symbol: "SEC24A"
type: "gene"
col: 3483
ensembl_id: "ENSG00000113615"
name: "SEC24 homolog A, COPII component"
location: "5q31.1"
module: 56
arm: "+"
pooled_cpm: 214.21
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SEC24A

*SEC24 homolog A, COPII component* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.36× (z +10.2, q 1e-21, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.346× (z -11.9, q 9e-30, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.453× (z -9.2, q 5e-18, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARF4]] (+0.76, fdr 7e-06), [[PGM3]] (+0.75, fdr 7e-06), [[KDELR2]] (+0.73, fdr 7e-06); moves opposite to [[ZNF236]] (-0.56, fdr 3e-05), [[DLG5]] (-0.54, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.36×** | +10.2 | 1e-21 | 47/49 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +5.6 | 7e-06 | 41/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.3 | 0.003 | 38/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.94×** | +4.0 | 0.008 | 39/48 (CFPAC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.015 | 42/48 (MIA PaCa-2, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +3.6 | 0.026 | 30/48 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.22× | +3.2 | 0.11 | 24/49 (J82, RKO, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.32× | +3.2 | 0.11 | 28/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[EX229 (drug)]] 0.05 µM |  | 1.32× | +3.1 | 0.14 | 30/48 (Hs 766T, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3483.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.346×** | -11.9 | 9e-30 | 39/44 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.370×** | -11.6 | 2e-28 | 44/49 (CFPAC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.453×** | -9.2 | 5e-18 | 44/48 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.456×** | -9.1 | 9e-18 | 44/48 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.523×** | -7.3 | 4e-11 | 46/48 (RKO, J82, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.536×** | -7.0 | 3e-10 | 42/47 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.681×** | -6.3 | 2e-08 | 41/48 (C32, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.691×** | -6.1 | 8e-08 | 41/48 (HS-578T, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.596×** | -6.0 | 1e-07 | 40/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.606×** | -5.4 | 4e-06 | 33/45 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.652×** | -5.0 | 3e-05 | 39/48 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.674×** | -4.6 | 2e-04 | 33/48 (SW 900, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.682×** | -4.5 | 4e-04 | 42/48 (A549, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.529×** | -3.9 | 0.004 | 36/49 (HS-578T, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -3.8 | 0.006 | 32/48 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -3.7 | 0.008 | 30/48 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.729×** | -3.7 | 0.008 | 32/48 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.738×** | -3.5 | 0.012 | 29/48 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.748×** | -3.4 | 0.019 | 35/48 (SW 1088, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 399 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.64× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.326× (z -12.3) |
| [[HS-578T (line)]] | alt | 361 | 5 (2 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.6× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.343× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 305 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 14.2× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.319× (z -11.1) |
| [[SW 900 (line)]] | alt | 251 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.02× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.269× (z -12.3) |
| [[A498 (line)]] | wt | 273 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.416× (z -11.2) |
| [[J82 (line)]] | alt | 249 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.36× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.437× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 299 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.83× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.356× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 275 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.321× (z -12.4) |
| [[H4 (line)]] | wt | 342 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.31× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.294× (z -10.6) |
| [[LoVo (line)]] | wt | 248 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.54× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.331× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 222 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.349× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 205 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.40× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.396× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 177 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.47× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.21× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 283 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.13× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.506× (z -9.0) |
| [[A-172 (line)]] | wt | 218 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.89× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -12.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 298 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.346× (z -12.2) |
| [[HOP62 (line)]] | alt | 345 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.91× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.292× (z -9.4) |
| [[Hs 766T (line)]] | wt | 247 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.368× (z -8.8) |
| [[HT-29 (line)]] | alt | 177 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.347× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 209 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.362× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 325 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.46× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 293 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.20× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -9.2) |
| [[PANC-1 (line)]] | alt | 170 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 77.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.95× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 200 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.65× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -18.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 197 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.92× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.250× (z -11.4) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 122 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -15.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 235 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.96× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -10.4) ⚠ cell-cycle shift, explains ~12% of this change |
| [[KATO III (line)]] | alt | 127 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.401× (z -9.3) |
| [[RKO (line)]] | wt | 213 | 0 | 2 (1 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.233× (z -10.2) |
| [[SHP-77 (line)]] | alt | 89.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.96× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.102× (z -19.4) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 363 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -12.2) |
| [[C-33 A (line)]] | alt | 61.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +8.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -10.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 223 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 322 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -10.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.411× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 297 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -12.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 144 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 104 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 127 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARF4]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PGM3]] | +0.75 | +0.67 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[KDELR2]] | +0.73 | +0.76 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SRP54]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 997 |
| [[SEC31A]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 996 |
| [[HM13]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[SUCO]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.67 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF236]] | -0.56 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[DLG5]] | -0.54 | -0.57 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, -34.9); signed map (-50.9, 11.9). **Vector** length 124, 54.1% of its response variance represented; |z| ≥ 3 in 1,602 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *protein secretion* (hallmark, mean cos +0.56 to 10); *COPI-dependent Golgi-to-ER retrograde traffic* (reactome, mean cos +0.60 to 9); *COPI-mediated anterograde transport* (reactome, mean cos +0.60 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +7.9 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.4 | -3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[EX229 (drug)]] 0.05 µM |  | +3.2 | +3.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.8 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.3 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.8 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.6 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.5 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | SEC24 homolog A, COPII component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,648,785-134,727,909 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Coat protein complex II |
| Reactome | 19 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; Cargo concentration in the ER; Regulation of cholesterol biosynthesis by SREBP (SREBF) |
| Matched by | ensembl_id |

**Function**, from UniProt [O95486](https://www.uniprot.org/uniprotkb/O95486) (Protein transport protein Sec24A):

> Component of the coat protein complex II (COPII) which promotes the formation of transport vesicles from the endoplasmic reticulum (ER). The coat has two main functions, the physical deformation of the endoplasmic reticulum membrane into vesicles and the selection of cargo molecules for their transport to the Golgi complex. Plays a central role in cargo selection within the COPII complex and together with SEC24B may have a different specificity compared to SEC24C and SEC24D. May package …

**Summary**, from NCBI Gene [10802](https://www.ncbi.nlm.nih.gov/gene/10802):

> The protein encoded by this gene belongs to a family of proteins that are homologous to yeast Sec24. This protein is a component of coat protein II (COPII)-coated vesicles that mediate protein transport from the endoplasmic reticulum. COPII acts in the cytoplasm to promote the transport of secretory, plasma membrane, and vacuolar proteins from the endoplasmic reticulum to the golgi complex. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:10703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10703) · Entrez [10802](https://www.ncbi.nlm.nih.gov/gene/10802) · UniProt [O95486](https://www.uniprot.org/uniprotkb/O95486) · Ensembl [ENSG00000113615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113615)

## Data

Gene col 3483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3483); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3483]; `tensor/DDL_lfc|DDL_z.npy` [3483]; `embed/gene_vectors.npy` [3483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3483 or target_col == 3483). Every well: [[SEC24A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC24A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
