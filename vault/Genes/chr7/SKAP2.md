---
symbol: "SKAP2"
type: "gene"
col: 62
ensembl_id: "ENSG00000005020"
name: "src kinase associated phosphoprotein 2"
location: "7p15.2"
module: 5
arm: "-"
pooled_cpm: 219.75
n_lines_expressing: 47
n_dd_up: 20
n_dd_down: 32
n_dd_up_clean: 18
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SKAP2

*src kinase associated phosphoprotein 2* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +9.6, q 4e-19, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.408× (z -18.7, q 0e+00, down in 43 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.442× (z -17.1, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OPTN]] (+0.64, fdr 7e-06), [[DAAM1]] (+0.63, fdr 7e-06), [[KMT2C]] (+0.62, fdr 1e-05); moves opposite to [[DHX33]] (-0.62, fdr 1e-05), [[ZNF718]] (-0.59, fdr 1e-05), [[WDR4]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 6 go from it, the strongest it → cells under [[Afatinib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 62.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +9.6 | 4e-19 | 39/45 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +9.2 | 1e-17 | 42/45 (A498, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +7.9 | 8e-13 | 35/45 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +7.2 | 8e-11 | 29/45 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +6.5 | 7e-09 | 35/44 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +6.0 | 1e-07 | 30/46 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +5.8 | 5e-07 | 28/45 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +5.7 | 7e-07 | 38/46 (LoVo, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +5.4 | 3e-06 | 24/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +5.2 | 9e-06 | 24/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +4.6 | 2e-04 | 24/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +4.6 | 2e-04 | 26/45 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +4.6 | 2e-04 | 26/44 (SK-MEL-2, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.23×** | +4.5 | 2e-04 | 25/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 4e-04 | 25/44 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 5e-04 | 22/45 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 62.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.408×** | -18.7 | 0e+00 | 43/45 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.442×** | -17.1 | 0e+00 | 43/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.473×** | -15.7 | 0e+00 | 40/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.489×** | -14.3 | 2e-44 | 38/44 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.545×** | -12.7 | 8e-35 | 40/45 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.557×** | -12.2 | 3e-32 | 39/45 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.573×** | -11.6 | 3e-29 | 38/45 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.567×** | -11.4 | 3e-28 | 39/44 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.434×** | -8.6 | 7e-16 | 42/46 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.666×** | -8.5 | 1e-15 | 39/45 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.486×** | -7.4 | 7e-12 | 37/45 (Panc 03.27, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.704×** | -6.9 | 2e-10 | 33/45 (LoVo, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -6.5 | 3e-09 | 30/45 (CFPAC-1, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.542×** | -6.3 | 1e-08 | 36/45 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.741×** | -6.3 | 1e-08 | 26/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.830×** | -5.5 | 1e-06 | 22/46 (H4, RPMI-7951, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.770×** | -5.5 | 1e-06 | 29/45 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.597×** | -5.3 | 3e-06 | 32/45 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.781×** | -5.1 | 7e-06 | 28/45 (NCI-H1573, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 62. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 229 | 9 (3 ⚠) | 10 (5 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.11× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.266× (z -18.7) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.420× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 476 | 2 | 15 (11 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.74× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -21.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.280× (z -17.8) |
| [[SW480 (line)]] | alt | 197 | 0 | 12 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -24.1) |
| [[LoVo (line)]] | wt | 242 | 3 | 8 (2 ⚠) | [[Belinostat (drug)]] 5 µM 1.99× (z +11.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.421× (z -13.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.482× (z -12.1) |
| [[PANC-1 (line)]] | alt | 207 | 3 | 8 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.18× (z +11.4) | [[Digitoxin (drug)]] 0.5 µM 0.333× (z -16.3) |
| [[A-172 (line)]] | wt | 173 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -11.9) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.422× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 157 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.352× (z -15.0) |
| [[SNU-423 (line)]] | alt | 187 | 1 | 9 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.01× (z +11.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.353× (z -11.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.382× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 287 | 2 | 7 (4 ⚠) | [[Retinoic acid (drug)]] 5 µM 1.89× (z +11.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.253× (z -17.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 332 | 0 | 9 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.256× (z -15.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.358× (z -12.4) |
| [[SW1417 (line)]] | alt | 253 | 5 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.88× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -13.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.478× (z -9.7) |
| [[Hs 766T (line)]] | wt | 223 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.229× (z -15.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -12.7) |
| [[SW 900 (line)]] | alt | 323 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.353× (z -12.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.449× (z -10.1) |
| [[A498 (line)]] | wt | 437 | 5 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 2.06× (z +11.7) | [[Auranofin (drug)]] 5 µM 0.508× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 266 | 1 | 6 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.67× (z +9.4) | [[Ixazomib citrate (drug)]] 5 µM 0.398× (z -11.8) |
| [[KATO III (line)]] | alt | 241 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.01× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.235× (z -17.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.441× (z -10.2) |
| [[LS 180 (line)]] | wt | 183 | 1 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.9) ⚠ cell-cycle shift, explains ~85% of this change | [[Digitoxin (drug)]] 5 µM 0.374× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.413× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.266× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.308× (z -11.1) |
| [[A549 (line)]] | wt | 220 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.7) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.351× (z -10.6) |
| [[C32 (line)]] | wt | 197 | 0 | 6 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -15.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -12.9) |
| [[SHP-77 (line)]] | alt | 100 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.372× (z -11.6) |
| [[J82 (line)]] | alt | 158 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.433× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 98.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.337× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 794 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -15.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[COLO 205 (line)]] | alt | 198 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.6) ⚠ cell-cycle shift, explains ~85% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.303× (z -14.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.415× (z -10.7) |
| [[HOP62 (line)]] | alt | 91.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 0.5 µM 0.395× (z -10.5) |
| [[HT-29 (line)]] | alt | 215 | 3 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.81× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.335× (z -14.4) ⚠ toxic |
| [[H4 (line)]] | wt | 255 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.405× (z -8.8) |
| [[HS-578T (line)]] | alt | 203 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.367× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.372× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 239 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.461× (z -11.0) |
| [[SW48 (line)]] | wt | 114 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 3.64× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.290× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.296× (z -8.5) |
| [[A-427 (line)]] | wt | 134 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.30× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[HCT15 (line)]] | alt | 122 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 334 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.361× (z -13.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.527× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 158 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 91.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.327× (z -11.1) |
| [[RKO (line)]] | wt | 148 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.7) ⚠ cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[AN3 CA (line)]] | alt | 287 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.326× (z -10.1) |
| [[SW 1088 (line)]] | alt | 240 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0578× (z -13.4) |
| [[SW 1271 (line)]] | alt | 152 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.153× (z -10.5) |
| [[BT-474 (line)]] | alt | 45.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 123 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 62), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPTN]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[DAAM1]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[KMT2C]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[SPAG9]] | +0.58 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[RIOK3]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[DCAF6]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[SHOC2]] | +0.55 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[LMNA]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CTR9]] | +0.54 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[TUBA1A]] | +0.53 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[LIFR]] | +0.53 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[NBEAL1]] | +0.53 | +0.51 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX33]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[ZNF718]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[WDR4]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | -0.58 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[TRNT1]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[COX10]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[ALG8]] | -0.57 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ARMC6]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | -0.57 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[MSANTD2]] | -0.56 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[NADK]] | -0.56 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[XPO4]] | -0.56 | -0.56 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers SKAP2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[FBXO32]] | B | FBXO32 activity raises SKAP2's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.39× lower at baseline in the lines without FBXO32 | 0.066 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Afatinib (drug)]] 5 µM | C | SKAP2 activity raises the cells' numbers under Afatinib 5 µM (protects the cells) | lines that do not express SKAP2 (3) vs lines expressing it (45) | the lines without SKAP2: 0.67× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: IGF2BP2, TCF7, TRIB3; maybe low, not absent |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | SKAP2 activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express SKAP2 (3) vs lines expressing it (45) | the lines without SKAP2: 1.42× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: IGF2BP2, TCF7, TRIB3; maybe low, not absent |
| cells under [[Trametinib (drug)]] 5 µM | C | SKAP2 activity raises the cells' numbers under Trametinib 5 µM (protects the cells) | lines that do not express SKAP2 (3) vs lines expressing it (45) | the lines without SKAP2: 0.64× the cells of the other lines | 0.041 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: IGF2BP2, TCF7, TRIB3; maybe low, not absent |
| cells under [[PF-06260933 (drug)]] 5 µM | C | SKAP2 activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express SKAP2 (3) vs lines expressing it (45) | the lines without SKAP2: 1.58× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: IGF2BP2, TCF7, TRIB3; maybe low, not absent |
| cells under [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM | C | SKAP2 activity raises the cells' numbers under Trametinib (DMSO_TF solvate) 0.5 µM (protects the cells) | lines that do not express SKAP2 (3) vs lines expressing it (45) | the lines without SKAP2: 0.74× the cells of the other lines | 0.079 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: IGF2BP2, TCF7, TRIB3; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | C | SKAP2 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SKAP2 (3) vs lines expressing it (45) | the lines without SKAP2: 0.58× the cells of the other lines | 0.087 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: IGF2BP2, TCF7, TRIB3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.6, -43.2); signed map (-18.2, 23.1). **Vector** length 115, 41.9% of its response variance represented; |z| ≥ 3 in 1,937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +9.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.4 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +6.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.2 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +9.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +4.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -12.9 | -14.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -10.0 | -12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -8.0 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | -5.9 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -6.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | +2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | src kinase associated phosphoprotein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:26,667,068-26,995,239 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RA70, SKAP-HOM, SKAP55R, SAPS; previously SCAP2 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; SH3 domain containing |
| Hallmark sets | APICAL_JUNCTION, MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: Signal regulatory protein family interactions; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [O75563](https://www.uniprot.org/uniprotkb/O75563) (Src kinase-associated phosphoprotein 2):

> May be involved in B-cell and macrophage adhesion processes. In B-cells, may act by coupling the B-cell receptor (BCR) to integrin activation. May play a role in src signaling pathway.

**Summary**, from NCBI Gene [8935](https://www.ncbi.nlm.nih.gov/gene/8935):

> The protein encoded by this gene shares homology with Src kinase-associated phosphoprotein 1, and is a substrate of Src family kinases. It is an adaptor protein that is thought to play an essential role in the Src signaling pathway, and in regulating proper activation of the immune system. This protein contains an amino terminal coiled-coil domain for self-dimerization, a plecskstrin homology (PH) domain required for interactions with lipids at the membrane, and a Src homology (SH3) domain at …

**Accessions** — [HGNC:15687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15687) · Entrez [8935](https://www.ncbi.nlm.nih.gov/gene/8935) · UniProt [O75563](https://www.uniprot.org/uniprotkb/O75563) · Ensembl [ENSG00000005020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005020)

## Data

Gene col 62: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 62); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 62, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 62]; `tensor/DDL_lfc|DDL_z.npy` [62]; `embed/gene_vectors.npy` [62]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 62 or target_col == 62). Every well: [[SKAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
