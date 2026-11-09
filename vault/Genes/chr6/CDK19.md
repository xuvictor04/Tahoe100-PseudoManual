---
symbol: "CDK19"
type: "gene"
col: 7873
ensembl_id: "ENSG00000155111"
name: "cyclin dependent kinase 19"
location: "6q21"
module: 234
arm: "+"
pooled_cpm: 222.65
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 41
n_dd_up_clean: 7
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/234"]
generated_by: "tahoemap"
---

# CDK19

*cyclin dependent kinase 19* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +9.9, q 3e-20, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.340× (z -21.2, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.408× (z -18.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CERT1]] (+0.69, fdr 1e-05), [[DLEU2]] (+0.68, fdr 7e-06), [[GPBP1L1]] (+0.67, fdr 7e-06); moves opposite to [[EIF2B3]] (-0.66, fdr 7e-06), [[AGK]] (-0.66, fdr 7e-06), [[RABGGTB]] (-0.62, fdr 1e-05).
> It is in [[Module 234]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7873.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +9.9 | 3e-20 | 32/49 (NCI-H23, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.6 | 7e-12 | 37/48 (HS-578T, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.3 | 4e-08 | 34/50 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.61×** | +5.1 | 6e-05 | 37/49 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.7 | 3e-04 | 28/47 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.27×** | +4.6 | 3e-04 | 31/50 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.009 | 30/50 (AsPC-1, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.024 | 20/48 (AsPC-1, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.6 | 0.024 | 22/48 (HS-578T, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.029 | 16/48 (KATO III, A-172, …) | rises with dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.033 | 17/48 (KATO III, SW 1088, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.4 | 0.033 | 18/49 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.058 | 18/48 (AsPC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.094 | 14/48 (HCT15, AN3 CA, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.094 | 10/49 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7873.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.340×** | -21.2 | 0e+00 | 42/44 (PANC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.389×** | -19.3 | 0e+00 | 48/49 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.408×** | -18.3 | 0e+00 | 46/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.450×** | -16.3 | 0e+00 | 48/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.422×** | -16.3 | 0e+00 | 43/45 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.451×** | -15.6 | 0e+00 | 46/47 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.517×** | -13.4 | 3e-39 | 46/48 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.529×** | -12.9 | 3e-36 | 45/48 (PANC-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.639×** | -12.6 | 2e-34 | 35/48 (HT-29, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.559×** | -11.4 | 2e-28 | 40/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.575×** | -11.3 | 8e-28 | 42/48 (A549, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.587×** | -10.8 | 2e-25 | 44/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.590×** | -10.7 | 3e-25 | 45/48 (A549, HCT15, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.591×** | -10.7 | 3e-25 | 45/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.596×** | -10.5 | 2e-24 | 42/48 (SW480, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.378×** | -10.4 | 1e-23 | 48/49 (PANC-1, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.439×** | -8.8 | 5e-17 | 45/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.442×** | -8.7 | 1e-16 | 47/48 (HT-29, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.447×** | -8.6 | 3e-16 | 44/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.451×** | -8.5 | 6e-16 | 44/48 (NCI-H1792, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.674×** | -8.0 | 4e-14 | 42/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.508×** | -7.2 | 1e-11 | 42/48 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.703×** | -6.2 | 1e-08 | 36/48 (HT-29, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.611×** | -5.2 | 3e-06 | 37/47 (SW48, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.629×** | -4.9 | 2e-05 | 28/48 (SNU-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 569 | 0 | 21 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.471× (z -12.4) |
| [[SW480 (line)]] | alt | 204 | 1 | 17 (10 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.341× (z -16.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -16.4) |
| [[MIA PaCa-2 (line)]] | alt | 362 | 2 | 13 (9 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -14.6) |
| [[HT-29 (line)]] | alt | 306 | 0 | 14 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.223× (z -18.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -17.0) |
| [[C32 (line)]] | wt | 372 | 0 | 13 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.372× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 228 | 0 | 13 (8 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.197× (z -21.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -17.4) |
| [[A549 (line)]] | wt | 189 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.437× (z -10.0) |
| [[HOP62 (line)]] | alt | 275 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 122 | 2 | 10 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.216× (z -19.5) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.398× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 249 | 1 | 10 (9 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -11.9) |
| [[A-172 (line)]] | wt | 230 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -15.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -12.2) |
| [[HCT15 (line)]] | alt | 386 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -12.7) |
| [[SNU-423 (line)]] | alt | 432 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.340× (z -14.8) |
| [[Hs 766T (line)]] | wt | 175 | 1 | 8 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -16.0) |
| [[COLO 205 (line)]] | alt | 137 | 1 | 7 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.202× (z -15.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 243 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -10.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.407× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 301 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -11.4) |
| [[KATO III (line)]] | alt | 298 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.413× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 198 | 2 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.441× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 284 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.435× (z -9.7) |
| [[H4 (line)]] | wt | 278 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -9.6) |
| [[LoVo (line)]] | wt | 199 | 1 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 225 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.350× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 128 | 2 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.331× (z -11.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 295 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.397× (z -11.2) |
| [[SW 900 (line)]] | alt | 189 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 153 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -11.5) |
| [[CHP-212 (line)]] | wt | 281 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 162 | 2 | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 129 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +11.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.464× (z -9.5) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 374 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -15.5) |
| [[HS-578T (line)]] | alt | 155 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.465× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 112 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +13.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -8.5) |
| [[SW48 (line)]] | wt | 182 | 1 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.357× (z -9.5) |
| [[A-427 (line)]] | wt | 231 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[CFPAC-1 (line)]] | alt | 98.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 186 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.428× (z -11.8) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 115 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.265× (z -13.6) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -12.9) |
| [[C-33 A (line)]] | alt | 232 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 160 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.403× (z -8.7) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.289× (z -14.4) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.393× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 132 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +12.3) | — |
| [[SW 1088 (line)]] | alt | 257 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERT1]] | +0.69 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[DLEU2]] | +0.68 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[GPBP1L1]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[KLHL24]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[LEPR]] | +0.67 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[PIK3CA]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[CEP57]] | +0.65 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[BBX]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NARF]] | +0.64 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[RSRP1]] | +0.63 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[KLRD1]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B3]] | -0.66 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[AGK]] | -0.66 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[RABGGTB]] | -0.62 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[CCT2]] | -0.60 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[POLR3B]] | -0.60 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[ALKBH8]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[RAD51D]] | -0.58 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[AGPS]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[DNAJC14]] | -0.58 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[POLR3H]] | -0.58 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TMEM177]] | -0.58 | -0.48 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDK19's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 234]]; 5 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.7, -42.7); signed map (-12.3, 9.7). **Vector** length 130, 54.7% of its response variance represented; |z| ≥ 3 in 1,815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +12.7 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.4 | +9.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +12.3 | +6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.8 | +0.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +0.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +0.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.1 | -16.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.8 | -10.7 |
|  | [[EX229 (drug)]] 5 µM |  | -6.7 | -8.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.3 | -8.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.2 | -8.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.3 | -7.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.8 | -8.5 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:110,609,978-110,815,958 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1028, bA346C16.3; previously CDK11, CDC2L6 |
| Gene groups (HGNC) | Cyclin dependent kinases; Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWU1](https://www.uniprot.org/uniprotkb/Q9BWU1) (Cyclin-dependent kinase 19):

> Component of the Mediator complex, a transcriptional coactivator required for regulated expression of nearly all RNA polymerase II-dependent genes. Acts as a molecular bridge between gene-specific regulatory proteins and the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters through direct interactions with transcriptional regulators and serves as a scaffold for assembly of the pre-initiation complex with RNA polymerase II and general transcription factors. …

**Summary**, from NCBI Gene [23097](https://www.ncbi.nlm.nih.gov/gene/23097):

> This gene encodes a protein that is one of the components of the Mediator co-activator complex. The Mediator complex is a multi-protein complex required for transcriptional activation by DNA binding transcription factors of genes transcribed by RNA polymerase II. The protein encoded by this gene is similar to cyclin-dependent kinase 8 which can also be a component of the Mediator complex. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by …

**Accessions** — [HGNC:19338](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19338) · Entrez [23097](https://www.ncbi.nlm.nih.gov/gene/23097) · UniProt [Q9BWU1](https://www.uniprot.org/uniprotkb/Q9BWU1) · Ensembl [ENSG00000155111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155111)

## Data

Gene col 7873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7873); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7873]; `tensor/DDL_lfc|DDL_z.npy` [7873]; `embed/gene_vectors.npy` [7873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7873 or target_col == 7873). Every well: [[CDK19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
