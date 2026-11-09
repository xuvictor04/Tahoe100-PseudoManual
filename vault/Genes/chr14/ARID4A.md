---
symbol: "ARID4A"
type: "gene"
col: 404
ensembl_id: "ENSG00000032219"
name: "AT-rich interaction domain 4A"
location: "14q23.1"
module: 69
arm: "+"
pooled_cpm: 129.88
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# ARID4A

*AT-rich interaction domain 4A* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.99× (z +36.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.485× (z -16.8, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.539× (z -7.5, q 7e-12, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBXN7]] (+0.75, fdr 7e-06), [[PLAG1]] (+0.73, fdr 7e-06), [[AAMDC]] (+0.73, fdr 7e-06); moves opposite to [[CLPB]] (-0.71, fdr 7e-06), [[EFTUD2]] (-0.70, fdr 7e-06), [[TMEM33]] (-0.69, fdr 7e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GRB7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 404.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.99×** | +36.0 | 0e+00 | 48/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +19.9 | 0e+00 | 44/49 (Panc 03.27, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +18.4 | 0e+00 | 44/48 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.00×** | +15.5 | 0e+00 | 45/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +14.4 | 3e-45 | 46/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +13.4 | 1e-38 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +12.8 | 8e-36 | 34/48 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +11.2 | 3e-27 | 35/50 (Panc 03.27, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +11.0 | 4e-26 | 40/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +9.1 | 5e-18 | 36/48 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +8.6 | 6e-16 | 43/48 (SW1417, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.40×** | +7.8 | 3e-13 | 28/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +7.0 | 1e-10 | 37/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.28×** | +5.8 | 3e-07 | 28/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +4.7 | 1e-04 | 26/49 (NCI-H2030, SNU-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +4.2 | 8e-04 | 25/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.038 | 8/48 (J82, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.10× | +3.1 | 0.053 | 4/48 (SNU-1, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 404.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.485×** | -16.8 | 0e+00 | 48/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -14.0 | 7e-42 | 40/44 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.547×** | -12.5 | 1e-33 | 40/49 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.600×** | -11.0 | 8e-26 | 36/45 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.539×** | -7.5 | 7e-12 | 44/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.565×** | -6.9 | 4e-10 | 39/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.571×** | -6.8 | 8e-10 | 37/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.750×** | -6.4 | 9e-09 | 35/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.611×** | -6.0 | 1e-07 | 35/48 (CFPAC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.630×** | -5.6 | 1e-06 | 38/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.805×** | -4.8 | 7e-05 | 24/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -4.5 | 4e-04 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.841× | -3.6 | 0.014 | 23/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.864× | -3.4 | 0.027 | 10/48 (LS 180, Panc 03.27, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.865× | -3.4 | 0.029 | 13/49 (LS 180, A498, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.909× | -3.1 | 0.059 | 1/48 (COLO 205) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.779×** | -3.0 | 0.072 | 16/49 (NCI-H2347, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.838× | -2.9 | 0.094 | 14/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 0.839× | -2.9 | 0.097 | 12/49 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 163 | 10 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +25.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.256× (z -19.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.263× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 96.7 | 12 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +29.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.374× (z -15.3) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 152 | 11 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +20.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.457× (z -13.2) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 117 | 9 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +24.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.479× (z -10.6) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 68.0 | 11 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +22.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.434× (z -11.5) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 173 | 10 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +18.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.323× (z -12.1) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 141 | 8 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +23.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.437× (z -12.5) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 155 | 9 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +28.9) | [[Dinaciclib (drug)]] 5 µM 0.472× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 140 | 9 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +17.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -11.0) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 169 | 9 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +24.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.477× (z -11.0) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 113 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -12.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 103 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +23.3) | — |
| [[Panc 03.27 (line)]] | alt | 183 | 6 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +19.3) | [[Lonafarnib (drug)]] 5 µM 0.0883× (z -19.8) ⚠ toxic |
| [[C32 (line)]] | wt | 137 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +36.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -12.9) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 118 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 176 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 190 | 1 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.604× (z -8.5) |
| [[RKO (line)]] | wt | 111 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +19.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.409× (z -8.9) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 83.4 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +25.3) | — |
| [[A549 (line)]] | wt | 136 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 115 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +21.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -14.4) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 229 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -20.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 93.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +20.8) | — |
| [[NCI-H1792 (line)]] | alt | 142 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +25.2) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.527× (z -9.4) |
| [[SHP-77 (line)]] | alt | 179 | 3 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.632× (z -8.9) |
| [[A-427 (line)]] | wt | 110 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -16.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 69.7 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +14.8) | — |
| [[HT-29 (line)]] | alt | 121 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +21.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.469× (z -9.3) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 167 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.483× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 119 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +19.1) | — |
| [[SW 900 (line)]] | alt | 207 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -16.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 86.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 211 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -12.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 132 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 112 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -16.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 120 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -17.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 82.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 88.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +23.6) | — |
| [[COLO 205 (line)]] | alt | 131 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -15.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 105 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 148 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +17.6) | — |
| [[SNU-1 (line)]] | wt | 99.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.248× (z -10.2) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 130 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.6) | — |
| [[CHP-212 (line)]] | wt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -8.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 97.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.5) | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN7]] | +0.75 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[PLAG1]] | +0.73 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[AAMDC]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[GCC2]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[ATOSA]] | +0.71 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.70 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.69 | +0.70 / +0.71 | both halves | 7e-06 | STRING 467 |
| [[CIR1]] | +0.69 | +0.57 / +0.74 | both halves | 9e-06 |  |
| [[AKAP9]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ING2]] | +0.68 | +0.55 / +0.69 | both halves | 1e-05 | STRING 986 |
| [[GGNBP2]] | +0.67 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[OGA]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLPB]] | -0.71 | -0.68 / -0.69 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.70 | -0.73 / -0.68 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.69 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[RABGGTB]] | -0.67 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[PTPN11]] | -0.66 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[MRPS27]] | -0.65 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[WDR77]] | -0.65 | -0.64 / -0.61 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[CCT5]] | -0.64 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[MRPL42]] | -0.64 | -0.58 / -0.65 | both halves | 8e-06 |  |
| [[ABCF2]] | -0.64 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[SPTBN2]] | -0.64 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.64 | -0.63 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRB7]] | B | GRB7 activity raises ARID4A's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 1.31× lower at baseline in the lines without GRB7 | 0.076 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.1, -43.7); signed map (-12.7, 8.3). **Vector** length 131, 46.8% of its response variance represented; |z| ≥ 3 in 1,412 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +19.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.1 | +8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +12.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.5 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.1 | +0.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.1 | +1.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.6 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -15.8 | -16.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.0 | -11.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | -8.4 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.2 | -6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.1 | -14.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.8 | -7.5 |
|  | [[EX229 (drug)]] 5 µM |  | -7.8 | -5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.3 | -6.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.6 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | AT-rich interaction domain 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:58,298,504-58,373,887 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RBP1, RBP-1; previously RBBP1 |
| Gene groups (HGNC) | AT-rich interaction domain containing |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 6 pathways, smallest: HDACs deacetylate histones; Potential therapeutics for SARS; Chromatin modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [P29374](https://www.uniprot.org/uniprotkb/P29374) (AT-rich interactive domain-containing protein 4A):

> DNA-binding protein which modulates activity of several transcription factors including RB1 (retinoblastoma-associated protein) and AR (androgen receptor) (By similarity). May function as part of an mSin3A repressor complex. Has no intrinsic transcriptional activity (By similarity). Plays a role in the regulation of epigenetic modifications at the PWS/AS imprinting center near the SNRPN promoter, where it might function as part of a complex with RB1 and ARID4B (By similarity). Involved in …

**Summary**, from NCBI Gene [5926](https://www.ncbi.nlm.nih.gov/gene/5926):

> The protein encoded by this gene is a ubiquitously expressed nuclear protein. It binds directly, with several other proteins, to retinoblastoma protein (pRB) which regulates cell proliferation. pRB represses transcription by recruiting the encoded protein. This protein, in turn, serves as a bridging molecule to recruit HDACs and, in addition, provides a second HDAC-independent repression function. The encoded protein possesses transcriptional repression activity. Multiple alternatively spliced …

**Accessions** — [HGNC:9885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9885) · Entrez [5926](https://www.ncbi.nlm.nih.gov/gene/5926) · UniProt [P29374](https://www.uniprot.org/uniprotkb/P29374) · Ensembl [ENSG00000032219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000032219)

## Data

Gene col 404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 404); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 404]; `tensor/DDL_lfc|DDL_z.npy` [404]; `embed/gene_vectors.npy` [404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 404 or target_col == 404). Every well: [[ARID4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARID4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
