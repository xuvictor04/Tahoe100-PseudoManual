---
symbol: "KLHL28"
type: "gene"
col: 11034
ensembl_id: "ENSG00000179454"
name: "kelch like family member 28"
location: "14q21.2"
module: 41
arm: "+"
pooled_cpm: 67.36
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 18
n_dd_up_clean: 15
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# KLHL28

*kelch like family member 28* — 14q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +14.5, q 3e-45, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.508× (z -12.7, q 6e-34, down in 36 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 0.784× (z -4.7, q 3e-04, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MINDY2]] (+0.74, fdr 7e-06), [[AFTPH]] (+0.73, fdr 7e-06), [[ESCO1]] (+0.70, fdr 7e-06); moves opposite to [[PSMD1]] (-0.65, fdr 7e-06), [[TULP4]] (-0.64, fdr 7e-06), [[CHCHD3]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TTC28]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11034.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +14.5 | 3e-45 | 42/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +13.8 | 5e-41 | 46/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +12.9 | 1e-35 | 43/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +12.0 | 5e-31 | 43/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +11.4 | 4e-28 | 38/49 (HS-578T, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +8.1 | 6e-14 | 40/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +8.0 | 8e-14 | 37/47 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +7.0 | 2e-10 | 30/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +6.0 | 2e-07 | 28/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.4 | 5e-06 | 25/50 (Panc 03.27, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +5.1 | 2e-05 | 31/48 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.6 | 2e-04 | 26/48 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.5 | 3e-04 | 22/48 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.26×** | +4.5 | 3e-04 | 25/48 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 5e-04 | 27/49 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.004 | 19/49 (A498, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.508×** | -12.7 | 6e-34 | 36/42 (hTERT-HPNE, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.534×** | -12.2 | 9e-32 | 40/49 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.580×** | -9.8 | 2e-20 | 36/45 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.779×** | -4.9 | 2e-04 | 29/48 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.784×** | -4.7 | 3e-04 | 26/48 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.794×** | -4.5 | 6e-04 | 23/48 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.788×** | -4.5 | 6e-04 | 23/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.800×** | -4.3 | 9e-04 | 26/48 (HEC-1-A, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.800×** | -4.3 | 9e-04 | 25/49 (A498, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | **0.805×** | -4.1 | 0.003 | 25/47 (NCI-H2347, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -4.0 | 0.003 | 22/48 (CFPAC-1, HCT15, …) | two highest doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.815×** | -4.0 | 0.003 | 23/47 (hTERT-HPNE, HT-29, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.816×** | -4.0 | 0.003 | 23/49 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.833×** | -3.6 | 0.014 | 17/49 (NCI-H1792, C-33 A, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.833×** | -3.6 | 0.014 | 12/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.839× | -3.4 | 0.021 | 11/48 (LS 180, NCI-H2030, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.839× | -3.4 | 0.021 | 16/47 (A549, NCI-H460, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.843× | -3.3 | 0.027 | 12/49 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.844× | -3.2 | 0.043 | 15/47 (A549, NCI-H1573, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.851× | -3.1 | 0.045 | 15/48 (LS 180, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 79.8 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 118 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.430× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 107 | 1 | 5 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.86× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.527× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 49.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +20.7) | — |
| [[J82 (line)]] | alt | 47.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -9.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 57.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +14.1) | — |
| [[BT-474 (line)]] | alt | 54.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.89× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.342× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[MIA PaCa-2 (line)]] | alt | 67.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +12.6) | — |
| [[SW480 (line)]] | alt | 59.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -12.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -16.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 62.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 77.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 57.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.7) | — |
| [[SW48 (line)]] | wt | 76.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 40.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +8.8) | — |
| [[C32 (line)]] | wt | 36.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +13.5) | — |
| [[CHP-212 (line)]] | wt | 88.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -12.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 66.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -10.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 77.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -10.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 107 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 68.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +16.8) | — |
| [[SW 900 (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -11.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 65.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 74.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -10.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 77.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -11.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -15.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 70.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 58.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 50.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -10.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 64.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -17.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 57.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 86.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 64.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0816× (z -10.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 50.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +14.6) | — |
| [[SNU-1 (line)]] | wt | 52.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 51.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.3) | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY2]] | +0.74 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[AFTPH]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ESCO1]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SRP54]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[MMUT]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[DIS3]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[GOLPH3L]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[PEX13]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SEC22A]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[YIPF5]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[TGDS]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[CDK7]] | +0.64 | +0.62 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD1]] | -0.65 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[TULP4]] | -0.64 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[CHCHD3]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[PSMD11]] | -0.62 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[CLPB]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[HERC2P9-1]] | -0.60 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[PSME3]] | -0.59 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[GFM1]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[CCT5]] | -0.58 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.58 | -0.45 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity lowers KLHL28's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 1.16× higher at baseline in the lines without TTC28 | 0.034 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[TOP2A]] | B | TOP2A activity lowers KLHL28's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (5.1, -34.6); signed map (-13.1, 3.2). **Vector** length 108, 32.6% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.8 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +11.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +3.8 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.0 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.3 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.9 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.6 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -1.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.9 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.7 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.2 — chr14:44,924,324-45,042,322 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20081; previously BTBD5 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q9NXS3](https://www.uniprot.org/uniprotkb/Q9NXS3) carries no function annotation.

**Summary**, from NCBI Gene [54813](https://www.ncbi.nlm.nih.gov/gene/54813):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Predicted to be part of Cul3-RING ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19741](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19741) · Entrez [54813](https://www.ncbi.nlm.nih.gov/gene/54813) · UniProt [Q9NXS3](https://www.uniprot.org/uniprotkb/Q9NXS3) · Ensembl [ENSG00000179454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179454)

## Data

Gene col 11034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11034); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11034]; `tensor/DDL_lfc|DDL_z.npy` [11034]; `embed/gene_vectors.npy` [11034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11034 or target_col == 11034). Every well: [[KLHL28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
