---
symbol: "ARHGEF2"
type: "gene"
col: 3808
ensembl_id: "ENSG00000116584"
name: "Rho/Rac guanine nucleotide exchange factor 2"
location: "1q22"
module: 63
arm: "+"
pooled_cpm: 99.28
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 34
n_dd_up_clean: 15
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# ARHGEF2

*Rho/Rac guanine nucleotide exchange factor 2* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.68× (z +11.5, q 8e-28, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.475× (z -16.5, q 0e+00, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.366× (z -16.2, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIB3]] (+0.76, fdr 7e-06), [[SESN2]] (+0.70, fdr 7e-06), [[ADM2]] (+0.68, fdr 3e-05); moves opposite to [[ZNF608]] (-0.52, fdr 3e-05), [[TNS3]] (-0.50, fdr 1e-04), [[PCM1]] (-0.50, fdr 5e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **1.68×** | +11.5 | 8e-28 | 43/47 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.81×** | +9.6 | 3e-19 | 41/47 (SW480, SHP-77, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +8.3 | 2e-14 | 39/47 (SW480, SHP-77, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **1.52×** | +6.8 | 1e-09 | 35/47 (SHP-77, C32, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.33×** | +6.4 | 2e-08 | 29/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.46×** | +6.1 | 8e-08 | 32/46 (SHP-77, C32, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +6.0 | 1e-07 | 30/47 (LoVo, SHP-77, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +5.4 | 4e-06 | 30/47 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.0 | 5e-05 | 27/46 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 6e-05 | 30/47 (SW480, Hs 766T, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.22×** | +4.4 | 5e-04 | 23/48 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.30×** | +4.3 | 8e-04 | 28/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.002 | 23/48 (SHP-77, NCI-H1573, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.002 | 23/47 (SHP-77, C32, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.27×** | +3.9 | 0.004 | 24/47 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.62×** | +3.8 | 0.005 | 22/48 (SHP-77, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dabrafenib (drug)]] 5 µM |  | **1.59×** | +3.6 | 0.009 | 22/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tomivosertib (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.038 | 17/47 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.086 | 8/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3808.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.475×** | -16.5 | 0e+00 | 39/47 (HT-29, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.366×** | -16.2 | 0e+00 | 44/47 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.376×** | -15.8 | 0e+00 | 43/47 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.503×** | -10.7 | 2e-24 | 33/41 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.523×** | -10.5 | 2e-23 | 39/47 (HT-29, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.572×** | -8.3 | 8e-15 | 29/44 (RKO, H4, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.599×** | -8.3 | 1e-14 | 34/47 (A498, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.623×** | -7.3 | 2e-11 | 35/47 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -7.3 | 2e-11 | 28/48 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.638×** | -7.2 | 2e-11 | 33/47 (SW48, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.627×** | -7.2 | 2e-11 | 32/49 (A-172, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.665×** | -6.6 | 2e-09 | 31/47 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.679×** | -6.0 | 9e-08 | 27/47 (RKO, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.701×** | -5.7 | 4e-07 | 26/47 (H4, LS 180, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.721×** | -5.1 | 2e-05 | 25/46 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.732×** | -5.0 | 2e-05 | 27/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.753×** | -5.0 | 2e-05 | 27/48 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.805×** | -4.9 | 4e-05 | 27/47 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.731×** | -4.8 | 4e-05 | 27/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.767×** | -4.8 | 4e-05 | 27/47 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.547×** | -4.7 | 6e-05 | 31/46 (MIA PaCa-2, J82, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.772×** | -4.7 | 6e-05 | 28/47 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.763×** | -4.4 | 3e-04 | 26/47 (RKO, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 70.7 | 5 | 8 (4 ⚠) | [[Artesunate (drug)]] 5 µM 2.03× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -19.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.292× (z -16.3) |
| [[A-172 (line)]] | wt | 262 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -18.4) |
| [[H4 (line)]] | wt | 224 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -14.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -13.1) |
| [[PANC-1 (line)]] | alt | 108 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -15.2) |
| [[LoVo (line)]] | wt | 68.2 | 4 (1 ⚠) | 5 (3 ⚠) | [[5-Azacytidine (drug)]] 5 µM 2.69× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.270× (z -13.4) |
| [[LS 180 (line)]] | wt | 67.5 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -18.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.216× (z -14.4) |
| [[SHP-77 (line)]] | alt | 73.2 | 9 (2 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 3.95× (z +17.6) | — |
| [[HT-29 (line)]] | alt | 150 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -26.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.151× (z -18.3) |
| [[RKO (line)]] | wt | 106 | 1 | 7 (4 ⚠) | [[Artesunate (drug)]] 5 µM 1.89× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -24.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -12.6) |
| [[HS-578T (line)]] | alt | 128 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -15.3) |
| [[A498 (line)]] | wt | 151 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 166 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -18.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 116 | 1 | 5 (2 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.69× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -16.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -12.2) |
| [[SW48 (line)]] | wt | 111 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.151× (z -12.9) |
| [[J82 (line)]] | alt | 93.1 | 1 | 4 (2 ⚠) | [[Artesunate (drug)]] 5 µM 1.95× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.322× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 182 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -11.6) |
| [[KATO III (line)]] | alt | 43.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -16.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 76.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.388× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.359× (z -9.3) |
| [[SNU-423 (line)]] | alt | 120 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -13.3) |
| [[SW1417 (line)]] | alt | 44.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 76.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0776× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.335× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -14.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.403× (z -8.7) |
| [[SNU-1 (line)]] | wt | 40.8 | 2 | 1 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.80× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[C32 (line)]] | wt | 56.4 | 2 | 0 | [[Artesunate (drug)]] 5 µM 4.36× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 91.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.421× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 78.1 | 1 | 1 (1 ⚠) | [[5-Azacytidine (drug)]] 5 µM 2.73× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 95.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -11.5) |
| [[COLO 205 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 95.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -10.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 81.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.318× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 73.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -9.3) |
| [[SW 1088 (line)]] | alt | 98.9 | 0 | 1 (1 ⚠) | — | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 0.0661× (z -9.2) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIB3]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[SESN2]] | +0.70 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ADM2]] | +0.68 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[GTPBP2]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[GOT1]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PABPC1L]] | +0.67 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[CARS1]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[LINC00662]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SLC1A5]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[GARS1]] | +0.65 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[SLC1A4]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SARS1]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF608]] | -0.52 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[TNS3]] | -0.50 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[PCM1]] | -0.50 | -0.51 / -0.39 | both halves | 5e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[TET2]] | -0.48 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[ITGB8]] | -0.47 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[CASD1]] | -0.46 | -0.52 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARHGEF2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.0, 49.1); signed map (-11.9, 25.1). **Vector** length 130, 45.5% of its response variance represented; |z| ≥ 3 in 1,677 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.56 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.56 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.56 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.1 | +8.3 |
|  | [[Artesunate (drug)]] 5 µM |  | +8.7 | +11.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.6 | +5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +8.2 | +9.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +7.0 | +6.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +6.2 | +4.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +5.2 | +6.8 |
| fall | [[NG25 (drug)]] 5 µM |  | -6.3 | -4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.1 | -4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.6 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.2 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.0 | -5.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.9 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | Rho/Rac guanine nucleotide exchange factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,946,851-156,007,070 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LFP40, GEF-H1, KIAA0651, P40, Lfc, GEFH1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; MicroRNA protein coding host genes |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 12 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92974](https://www.uniprot.org/uniprotkb/Q92974) (Rho guanine nucleotide exchange factor 2):

> Activates Rho-GTPases by promoting the exchange of GDP for GTP. May be involved in epithelial barrier permeability, cell motility and polarization, dendritic spine morphology, antigen presentation, leukemic cell differentiation, cell cycle regulation, innate immune response, and cancer. Binds Rac-GTPases, but does not seem to promote nucleotide exchange activity toward Rac-GTPases, which was uniquely reported in PubMed:9857026. May stimulate instead the cortical activity of Rac. Inactive toward …

**Summary**, from NCBI Gene [9181](https://www.ncbi.nlm.nih.gov/gene/9181):

> Rho GTPases play a fundamental role in numerous cellular processes that are initiated by extracellular stimuli that work through G protein coupled receptors. The encoded protein may form complex with G proteins and stimulate rho-dependent signals. Alternatively spliced transcript variants encoding different isoforms have been identified.[provided by RefSeq, Jun 2009]

**Accessions** — [HGNC:682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:682) · Entrez [9181](https://www.ncbi.nlm.nih.gov/gene/9181) · UniProt [Q92974](https://www.uniprot.org/uniprotkb/Q92974) · Ensembl [ENSG00000116584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116584)

## Data

Gene col 3808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3808); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3808]; `tensor/DDL_lfc|DDL_z.npy` [3808]; `embed/gene_vectors.npy` [3808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3808 or target_col == 3808). Every well: [[ARHGEF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
