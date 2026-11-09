---
symbol: "GRB10"
type: "gene"
col: 2717
ensembl_id: "ENSG00000106070"
name: "growth factor receptor bound protein 10"
location: "7p12.1"
module: 81
arm: "+"
pooled_cpm: 341.76
n_lines_expressing: 39
n_dd_up: 16
n_dd_down: 30
n_dd_up_clean: 10
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 19
direction_downstream: 16
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# GRB10

*growth factor receptor bound protein 10* — 7p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.28× (z +5.3, q 4e-05, up in 23 of 37 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Dihydroartemisinin (drug)]] 5 µM: 1.40× (z +5.2, q 4e-05, up in 29 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.246× (z -21.4, q 0e+00, down in 37 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3KBP1]] (+0.65, fdr 7e-06), [[C6orf141]] (+0.57, fdr 1e-05), [[ARHGEF2]] (+0.56, fdr 2e-05); moves opposite to [[LATS2]] (-0.53, fdr 3e-05), [[GTF2I]] (-0.48, fdr 2e-04), [[LSM14A]] (-0.46, fdr 3e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[C6orf141]] → it (grade B ⚠); 16 go from it, the strongest it → [[TAF8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.28×** | +5.3 | 4e-05 | 23/37 (RKO, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.43×** | +5.2 | 4e-05 | 23/37 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.40×** | +5.2 | 4e-05 | 29/36 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +5.1 | 4e-05 | 25/36 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 1e-04 | 28/36 (SNU-423, SW48, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +4.7 | 2e-04 | 20/37 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.34×** | +4.4 | 7e-04 | 21/38 (SW480, SW1417, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +4.3 | 0.001 | 20/38 (NCI-H460, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +3.8 | 0.009 | 17/37 (HepG2/C3A, RKO, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.010 | 20/37 (RKO, LoVo, …) | two highest doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.010 | 21/37 (SW48, RKO, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.010 | 21/37 (Hs 766T, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.014 | 21/37 (SHP-77, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.014 | 24/37 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.046 | 16/37 (LoVo, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.070 | 17/37 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.246×** | -21.4 | 0e+00 | 37/37 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.267×** | -20.1 | 0e+00 | 37/37 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.287×** | -18.3 | 0e+00 | 35/35 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.328×** | -17.0 | 0e+00 | 35/37 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.473×** | -16.1 | 0e+00 | 34/38 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.365×** | -15.3 | 0e+00 | 36/38 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.373×** | -14.4 | 4e-45 | 35/36 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.577×** | -8.4 | 5e-15 | 32/37 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.633×** | -6.9 | 2e-10 | 36/37 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.646×** | -6.6 | 2e-09 | 27/37 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.659×** | -6.3 | 1e-08 | 32/37 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.653×** | -6.0 | 1e-07 | 26/36 (NCI-H2347, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.677×** | -5.9 | 2e-07 | 24/37 (NCI-H1573, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.671×** | -5.8 | 2e-07 | 24/37 (HS-578T, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.765×** | -5.7 | 4e-07 | 23/37 (NCI-H2347, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.759×** | -4.2 | 9e-04 | 27/38 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.632×** | -3.6 | 0.007 | 20/38 (HepG2/C3A, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.844× | -3.5 | 0.011 | 16/38 (HepG2/C3A, NCI-H2347, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.651×** | -3.4 | 0.016 | 20/36 (A549, H4, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.800×** | -3.4 | 0.017 | 20/37 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.806×** | -3.3 | 0.025 | 20/37 (NCI-H1573, HS-578T, …) | two highest doses |  |
| [[AZD-7648 (drug)]] 5 µM |  | **0.673×** | -3.1 | 0.035 | 18/37 (SW 900, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 558 | 0 | 15 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -27.1) |
| [[NCI-H2347 (line)]] | alt | 1,052 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0976× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -19.2) |
| [[LoVo (line)]] | wt | 340 | 2 (1 ⚠) | 10 (7 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.63× (z +11.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.00× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -24.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.217× (z -19.4) |
| [[A549 (line)]] | wt | 1,131 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0469× (z -25.8) |
| [[HepG2_C3A (line)]] | wt | 449 | 1 (1 ⚠) | 10 (3 ⚠) | [[Daptomycin (drug)]] 5 µM 2.61× (z +8.6) ⚠ unreliable plate only | [[Belinostat (drug)]] 5 µM 0.156× (z -16.6) |
| [[HOP62 (line)]] | alt | 586 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0813× (z -21.2) |
| [[KATO III (line)]] | alt | 284 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -16.6) |
| [[NCI-H1573 (line)]] | alt | 464 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -21.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.102× (z -19.6) |
| [[NCI-H1792 (line)]] | alt | 1,410 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0486× (z -27.8) |
| [[RPMI-7951 (line)]] | alt | 416 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -15.0) |
| [[A-172 (line)]] | wt | 211 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -17.3) |
| [[CFPAC-1 (line)]] | alt | 566 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.133× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 290 | 2 (1 ⚠) | 7 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.40× (z +8.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.74× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -23.0) |
| [[SW48 (line)]] | wt | 233 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 738 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0702× (z -25.3) |
| [[PANC-1 (line)]] | alt | 197 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -14.6) |
| [[SW 900 (line)]] | alt | 624 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -13.5) |
| [[A498 (line)]] | wt | 259 | 1 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.6) ⚠ cell-cycle shift, explains ~46% of this change | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -16.3) |
| [[Hs 766T (line)]] | wt | 652 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -18.0) |
| [[HT-29 (line)]] | alt | 191 | 1 (1 ⚠) | 6 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.86× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -16.6) |
| [[SNU-423 (line)]] | alt | 229 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -17.0) |
| [[H4 (line)]] | wt | 680 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.176× (z -14.1) |
| [[RKO (line)]] | wt | 113 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -16.6) |
| [[LS 180 (line)]] | wt | 417 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.205× (z -12.8) |
| [[SW480 (line)]] | alt | 149 | 1 (1 ⚠) | 4 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.55× (z +9.3) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 5 µM 0.264× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 153 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -10.6) |
| [[SW1417 (line)]] | alt | 140 | 2 (1 ⚠) | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.87× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -9.7) ⚠ toxic |
| [[BT-474 (line)]] | alt | 503 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.5) |
| [[J82 (line)]] | alt | 96.7 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.4) ⚠ cell-cycle shift, explains ~46% of this change | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 222 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.334× (z -9.1) |
| [[SHP-77 (line)]] | alt | 444 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 163 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 170 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -9.0) |
| [[A-427 (line)]] | wt | 84.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 114 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 79.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 67.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 32.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1,088 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 27.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3KBP1]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[C6orf141]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ARHGEF2]] | +0.56 | +0.61 / +0.47 | both halves | 2e-05 | same gene group |
| [[ACVR1]] | +0.55 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[FAM107B]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MMP1]] | +0.55 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[LRRFIP1]] | +0.54 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[TRPV3]] | +0.54 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[ARG2]] | +0.53 | +0.53 / +0.38 | both halves | 7e-05 |  |
| [[GK]] | +0.53 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[GCKR]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ERN1]] | +0.52 | +0.43 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LATS2]] | -0.53 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[GTF2I]] | -0.48 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[LSM14A]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[SHROOM3]] | -0.45 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[LINC01836]] | -0.45 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[PAXBP1]] | -0.45 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[STOM]] | -0.45 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[TAF8]] | -0.44 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[TNS3]] | -0.44 | -0.44 / -0.28 | both halves | 3e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 16, C 3. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C6orf141]] | B | C6orf141 activity raises GRB10's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 3.32× lower at baseline in the lines without C6orf141 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[WNT7B]] | B | WNT7B activity raises GRB10's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 3.47× lower at baseline in the lines without WNT7B | 0.003 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[RPLP0P2]] | B | RPLP0P2 activity raises GRB10's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 4.81× lower at baseline in the lines without RPLP0P2 | 0.009 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[PLEK2]] | B | PLEK2 activity raises GRB10's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.48× lower at baseline in the lines without PLEK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[PSD3]] | B | PSD3 activity raises GRB10's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 3.58× lower at baseline in the lines without PSD3 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[TNS3]] | B | TNS3 activity raises GRB10's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 4.23× lower at baseline in the lines without TNS3 | 0.023 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[DHRS9]] | B | DHRS9 activity raises GRB10's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 3.32× lower at baseline in the lines without DHRS9 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[LYPD3]] | B | LYPD3 activity raises GRB10's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 2.34× lower at baseline in the lines without LYPD3 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[LINC01705]] | B | LINC01705 activity raises GRB10's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 1.80× lower at baseline in the lines without LINC01705 | 0.071 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[LTBP1]] | B | LTBP1 activity raises GRB10's level | lines that do not express LTBP1 (15) vs lines expressing it (35) | 2.88× lower at baseline in the lines without LTBP1 | 0.078 | ⚠ within organs, on part of the lines |
| [[ABTB3]] | B | ABTB3 activity raises GRB10's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 2.72× lower at baseline in the lines without ABTB3 | 0.080 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[AADAC]] | B | AADAC activity raises GRB10's level | lines that do not express AADAC (34) vs lines expressing it (16) | 2.77× lower at baseline in the lines without AADAC | 0.080 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TAF8]] | B | GRB10 activity lowers TAF8's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 1.59× higher at baseline in the lines without GRB10 | 0.009 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[S100A16]] | B | GRB10 activity raises S100A16's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 3.85× lower at baseline in the lines without GRB10 | 0.013 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[NDRG1]] | B | GRB10 activity raises NDRG1's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 3.02× lower at baseline in the lines without GRB10 | 0.013 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[WNT7B]] | B | GRB10 activity raises WNT7B's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 3.44× lower at baseline in the lines without GRB10 | 0.036 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[ATP6V0D2]] | B | GRB10 activity raises ATP6V0D2's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 1.97× lower at baseline in the lines without GRB10 | 0.048 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[ATP2B1]] | B | GRB10 activity raises ATP2B1's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without GRB10 | 0.049 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[ZNF385A]] | B | GRB10 activity raises ZNF385A's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without GRB10 | 0.050 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[SMOX]] | B | GRB10 activity raises SMOX's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 2.50× lower at baseline in the lines without GRB10 | 0.057 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[TNS3]] | B | GRB10 activity raises TNS3's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 2.80× lower at baseline in the lines without GRB10 | 0.064 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[C6orf141]] | B | GRB10 activity raises C6orf141's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 2.68× lower at baseline in the lines without GRB10 | 0.072 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[PTHLH]] | B | GRB10 activity raises PTHLH's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 2.30× lower at baseline in the lines without GRB10 | 0.090 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[LTBP1]] | B | GRB10 activity raises LTBP1's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 2.39× lower at baseline in the lines without GRB10 | 0.090 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.8, -5.9); signed map (-5.7, 50.2). **Vector** length 105, 36.7% of its response variance represented; |z| ≥ 3 in 1,593 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.1 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +0.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.0 |
|  | [[NG25 (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | -3.5 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -3.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.0 | -2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.9 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.9 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | growth factor receptor bound protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.1 — chr7:50,590,063-50,793,462 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; SH2 domain containing; Growth factor receptor bound protein 7 family |
| Reactome | 14 pathways, smallest: IRS activation; Signal attenuation; Response of EIF2AK1 (HRI) to heme deficiency |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13322](https://www.uniprot.org/uniprotkb/Q13322) (Growth factor receptor-bound protein 10):

> Adapter protein which modulates coupling of a number of cell surface receptor kinases with specific signaling pathways. Binds to, and suppress signals from, activated receptors tyrosine kinases, including the insulin (INSR) and insulin-like growth factor (IGF1R) receptors. The inhibitory effect can be achieved by 2 mechanisms: interference with the signaling pathway and increased receptor degradation. Delays and reduces AKT1 phosphorylation in response to insulin stimulation. Blocks association …

**Summary**, from NCBI Gene [2887](https://www.ncbi.nlm.nih.gov/gene/2887):

> The product of this gene belongs to a small family of adapter proteins that are known to interact with a number of receptor tyrosine kinases and signaling molecules. This gene encodes a growth factor receptor-binding protein that interacts with insulin receptors and insulin-like growth-factor receptors. Overexpression of some isoforms of the encoded protein inhibits tyrosine kinase activity and results in growth suppression. This gene is imprinted in a highly isoform- and tissue-specific …

**Accessions** — [HGNC:4564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4564) · Entrez [2887](https://www.ncbi.nlm.nih.gov/gene/2887) · UniProt [Q13322](https://www.uniprot.org/uniprotkb/Q13322) · Ensembl [ENSG00000106070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106070)

## Data

Gene col 2717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2717); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2717]; `tensor/DDL_lfc|DDL_z.npy` [2717]; `embed/gene_vectors.npy` [2717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2717 or target_col == 2717). Every well: [[GRB10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRB10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
