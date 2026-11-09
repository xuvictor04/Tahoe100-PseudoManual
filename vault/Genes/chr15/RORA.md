---
symbol: "RORA"
type: "gene"
col: 923
ensembl_id: "ENSG00000069667"
name: "RAR related orphan receptor A"
location: "15q22.2"
module: 79
arm: "+"
pooled_cpm: 275.56
n_lines_expressing: 42
n_dd_up: 6
n_dd_down: 39
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 8
direction_downstream: 2
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# RORA

*RAR related orphan receptor A* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.22× (z +5.8, q 5e-06, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.491× (z -20.4, q 0e+00, down in 31 of 40 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXN3]] (+0.60, fdr 1e-05), [[RBPJ]] (+0.57, fdr 1e-05), [[MXI1]] (+0.56, fdr 1e-05); moves opposite to [[MAPKAPK5]] (-0.52, fdr 4e-05), [[RNASEH1]] (-0.49, fdr 3e-05), [[SLC35B3]] (-0.46, fdr 7e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ESRRG]] → it (grade B ⚠); 2 go from it, the strongest it → [[MLLT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.8 | 5e-06 | 24/40 (C32, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.31×** | +5.5 | 1e-05 | 26/41 (HEC-1-A, C32, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.55×** | +4.6 | 7e-04 | 24/40 (HOP62, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.003 | 20/41 (NCI-H1573, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.009 | 19/40 (SW 900, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.20×** | +3.8 | 0.014 | 20/40 (A549, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Roxadustat (drug)]] 5 µM |  | 1.19× | +3.4 | 0.052 | 19/40 (HepG2/C3A, SNU-423, …) | top dose only |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.079 | 10/41 (BT-474, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 27 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 923.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.491×** | -20.4 | 0e+00 | 31/40 (NCI-H1792, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.366×** | -19.5 | 0e+00 | 33/36 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.401×** | -18.5 | 0e+00 | 37/41 (Panc 03.27, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -15.5 | 0e+00 | 31/41 (SHP-77, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.446×** | -15.1 | 0e+00 | 31/37 (C32, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.490×** | -13.9 | 7e-42 | 36/39 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.490×** | -13.9 | 7e-42 | 34/39 (C32, NCI-H23, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.537×** | -12.6 | 2e-34 | 36/40 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.538×** | -12.5 | 3e-34 | 32/40 (LOX-IMVI, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.529×** | -12.4 | 2e-33 | 30/40 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.541×** | -11.9 | 4e-31 | 34/40 (hTERT-HPNE, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.595×** | -10.5 | 4e-24 | 33/40 (Panc 03.27, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.637×** | -9.1 | 3e-18 | 33/40 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.644×** | -8.6 | 4e-16 | 30/42 (C32, hTERT-HPNE, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.679×** | -7.8 | 2e-13 | 23/40 (NCI-H460, SW480, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.496×** | -7.4 | 4e-12 | 36/40 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.786×** | -6.9 | 2e-10 | 24/40 (SNU-1, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.544×** | -6.4 | 3e-09 | 32/40 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.574×** | -5.9 | 1e-07 | 30/40 (SHP-77, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.578×** | -5.8 | 2e-07 | 29/40 (LOX-IMVI, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.769×** | -5.3 | 3e-06 | 25/40 (H4, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.607×** | -5.3 | 3e-06 | 27/40 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.638×** | -4.8 | 4e-05 | 24/39 (BT-474, H4, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.741×** | -4.3 | 3e-04 | 29/41 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 1,816 | 0 | 20 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -26.5) |
| [[LOX-IMVI (line)]] | wt | 397 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -22.0) |
| [[NCI-H460 (line)]] | wt | 690 | 0 | 16 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -21.9) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -19.1) |
| [[RPMI-7951 (line)]] | alt | 347 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -23.7) |
| [[NCI-H23 (line)]] | alt | 228 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -24.0) |
| [[SNU-423 (line)]] | alt | 247 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -24.5) |
| [[C32 (line)]] | wt | 338 | 2 (1 ⚠) | 10 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.94× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -21.1) |
| [[CFPAC-1 (line)]] | alt | 189 | 2 (1 ⚠) | 9 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.89× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -15.1) |
| [[HEC-1-A (line)]] | alt | 298 | 2 (1 ⚠) | 9 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.74× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 298 | 4 (2 ⚠) | 7 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.79× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -14.9) |
| [[NCI-H2030 (line)]] | alt | 473 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 485 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -18.5) |
| [[SW 900 (line)]] | alt | 398 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -21.0) |
| [[hTERT-HPNE (line)]] | wt | 557 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0937× (z -27.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -21.0) |
| [[NCI-H1792 (line)]] | alt | 205 | 5 (3 ⚠) | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.36× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -27.9) |
| [[SNU-1 (line)]] | wt | 233 | 0 | 10 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.413× (z -11.9) |
| [[HCT15 (line)]] | alt | 573 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -15.9) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.393× (z -14.3) |
| [[C-33 A (line)]] | alt | 469 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -8.7) |
| [[H4 (line)]] | wt | 513 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.444× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 199 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -24.8) |
| [[SW480 (line)]] | alt | 169 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -17.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -12.5) |
| [[HOP62 (line)]] | alt | 441 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -20.4) |
| [[J82 (line)]] | alt | 191 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.531× (z -11.8) |
| [[A-427 (line)]] | wt | 195 | 1 (1 ⚠) | 5 (5 ⚠) | [[Selinexor (drug)]] 5 µM 1.93× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.330× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HepG2_C3A (line)]] | wt | 350 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -14.6) |
| [[LoVo (line)]] | wt | 299 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.445× (z -11.1) |
| [[SW 1271 (line)]] | alt | 749 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.3) |
| [[RKO (line)]] | wt | 183 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -12.0) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.279× (z -11.2) |
| [[A549 (line)]] | wt | 122 | 2 | 2 | [[Tucidinostat (drug)]] 5 µM 2.29× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.3) |
| [[LS 180 (line)]] | wt | 455 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -10.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SW1417 (line)]] | alt | 163 | 1 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.496× (z -9.4) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 105 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.383× (z -9.5) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.376× (z -9.3) |
| [[BT-474 (line)]] | alt | 357 | 2 (1 ⚠) | 1 (1 ⚠) | [[Neratinib (maleate) (drug)]] 0.5 µM 2.30× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Afatinib (drug)]] 5 µM 2.32× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.447× (z -8.7) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 69.7 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.81× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -8.8) |
| [[COLO 205 (line)]] | alt | 220 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.312× (z -11.4) ⚠ cell-cycle shift, explains ~60% of this change |
| [[Hs 766T (line)]] | wt | 166 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.442× (z -9.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[CHP-212 (line)]] | wt | 367 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -15.7) |
| [[HT-29 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.422× (z -8.7) ⚠ cell-cycle shift, explains ~69% of this change |
| [[SW 1088 (line)]] | alt | 200 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.124× (z -8.6) |
| [[A498 (line)]] | wt | 41.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 25.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 428 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 432 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 40.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 42.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXN3]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[RBPJ]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[MXI1]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[GAMT]] | +0.56 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[POU3F3]] | +0.56 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[HILPDA]] | +0.55 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[FAM13A]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[LINC02575]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ZNF292]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[SNAP25]] | +0.54 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[NOL4]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[NDRG1]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[RNASEH1]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SLC35B3]] | -0.46 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[DUS2]] | -0.46 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[TIMM23B-AGAP6]] | -0.46 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[AGAP5]] | -0.46 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[SCO1]] | -0.46 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[PRDM5]] | -0.46 | -0.48 / -0.28 | both halves | 3e-04 | STRING 422 |
| [[ARMC6]] | -0.45 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[DPH5-DT]] | -0.45 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[LINC01134]] | -0.45 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[PCBD2]] | -0.45 | -0.36 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESRRG]] | B | ESRRG activity raises RORA's level | lines that do not express ESRRG (26) vs lines expressing it (24) | 1.99× lower at baseline in the lines without ESRRG | 0.029 | ⚠ within organs, on part of the lines; also absent: HS3ST5, RUNX1T1, SNTG1; maybe low, not absent |
| [[MLLT3]] | B | MLLT3 activity raises RORA's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 3.40× lower at baseline in the lines without MLLT3 | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[GHR]] | B | GHR activity raises RORA's level | lines that do not express GHR (24) vs lines expressing it (26) | 1.97× lower at baseline in the lines without GHR | 0.058 | ⚠ within organs, on part of the lines; also absent: FAP, LHX2, ADCY1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RORA's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PDK4]] | B | PDK4 activity raises RORA's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 1.68× lower at baseline in the lines without PDK4 | 0.077 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[TOP2A]] | B | TOP2A activity raises RORA's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCTD16]] | B | KCTD16 activity raises RORA's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without KCTD16 | 0.090 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent |
| [[FAM13A]] | B | FAM13A activity raises RORA's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.74× lower at baseline in the lines without FAM13A | 0.094 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLLT3]] | B | RORA activity raises MLLT3's level | lines that do not express RORA (8) vs lines expressing it (42) | 3.31× lower at baseline in the lines without RORA | 0.016 | ⚠ within organs, on part of the lines; also absent: DPF3, TMC3-AS1 |
| [[IPMK]] | B | RORA activity raises IPMK's level | lines that do not express RORA (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without RORA | 0.067 | ⚠ within organs, on part of the lines; also absent: DPF3, TMC3-AS1 |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, -16.4); signed map (-34.2, 24.6). **Vector** length 108, 31.9% of its response variance represented; |z| ≥ 3 in 1,719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +7.2 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.2 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +6.9 | -18.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +5.2 | -5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.6 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -12.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.4 | -9.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -4.1 | -4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -7.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | -3.7 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.2 | -5.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -3.2 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.1 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | RAR related orphan receptor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:60,488,284-61,229,302 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RZRA, ROR1, ROR2, ROR3, NR1F1, ROR-alpha, RORalpha, RORa1 |
| Gene groups (HGNC) | RAR related orphan receptors |
| Hallmark sets | IL2_STAT5_SIGNALING, HYPOXIA |
| Reactome | 21 pathways, smallest: Phosphorylation of CLOCK, acetylation of BMAL1 (ARNTL) at target gene promoters; The CRY:PER:kinase complex represses transactivation by the BMAL:CLOCK (ARNTL:CLOCK) complex; Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P35398](https://www.uniprot.org/uniprotkb/P35398) (Nuclear receptor ROR-alpha):

> Nuclear receptor that binds DNA as a monomer to ROR response elements (RORE) containing a single core motif half-site 5'-AGGTCA-3' preceded by a short A-T-rich sequence. Key regulator of embryonic development, cellular differentiation, immunity, circadian rhythm as well as lipid, steroid, xenobiotics and glucose metabolism. Considered to have intrinsic transcriptional activity, have some natural ligands like oxysterols that act as agonists (25-hydroxycholesterol) or inverse agonists …

**Summary**, from NCBI Gene [6095](https://www.ncbi.nlm.nih.gov/gene/6095):

> The protein encoded by this gene is a member of the NR1 subfamily of nuclear hormone receptors. It can bind as a monomer or as a homodimer to hormone response elements upstream of several genes to enhance the expression of those genes. The encoded protein has been shown to interact with NM23-2, a nucleoside diphosphate kinase involved in organogenesis and differentiation, as well as with NM23-1, the product of a tumor metastasis suppressor candidate gene. Also, it has been shown to aid in the …

**Accessions** — [HGNC:10258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10258) · Entrez [6095](https://www.ncbi.nlm.nih.gov/gene/6095) · UniProt [P35398](https://www.uniprot.org/uniprotkb/P35398) · Ensembl [ENSG00000069667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069667)

## Data

Gene col 923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 923); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 923]; `tensor/DDL_lfc|DDL_z.npy` [923]; `embed/gene_vectors.npy` [923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 923 or target_col == 923). Every well: [[RORA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RORA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
