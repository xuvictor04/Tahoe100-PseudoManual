---
symbol: "ATG10"
type: "gene"
col: 7616
ensembl_id: "ENSG00000152348"
name: "autophagy related 10"
location: "5q14.1-q14.2"
module: 28
arm: "+"
pooled_cpm: 123.8
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 42
n_dd_up_clean: 12
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ATG10

*autophagy related 10* — 5q14.1-q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.49× (z +5.8, q 5e-06, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (22 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.265× (z -19.9, q 0e+00, down in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.269× (z -19.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GMDS-DT]] (+0.63, fdr 7e-06), [[IMMP2L]] (+0.61, fdr 1e-05), [[TBCK]] (+0.61, fdr 1e-05); moves opposite to [[RAPGEF3]] (-0.56, fdr 1e-05), [[ARHGEF1]] (-0.53, fdr 1e-05), [[CEP295NL]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +5.8 | 5e-06 | 39/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.42×** | +5.4 | 2e-05 | 37/50 (SW480, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 5e-04 | 32/48 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 5e-04 | 35/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 7e-04 | 30/48 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.33×** | +4.5 | 7e-04 | 32/49 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.004 | 32/48 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.006 | 31/48 (NCI-H2347, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.010 | 27/47 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.013 | 25/49 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.032 | 25/48 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.4 | 0.034 | 20/48 (LS 180, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.072 | 22/50 (NCI-H2347, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.095 | 20/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7616.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.265×** | -19.9 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.391×** | -19.9 | 0e+00 | 44/48 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.269×** | -19.7 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.348×** | -15.8 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.355×** | -14.9 | 0e+00 | 42/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.388×** | -14.2 | 1e-43 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.384×** | -13.8 | 3e-41 | 43/48 (NCI-H460, SK-MEL-2, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.429×** | -12.7 | 5e-35 | 47/48 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.436×** | -12.4 | 1e-33 | 43/48 (SW480, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.232×** | -11.4 | 2e-28 | 48/49 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.460×** | -11.2 | 3e-27 | 33/44 (C-33 A, A-427, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.494×** | -10.5 | 3e-24 | 38/48 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.470×** | -10.5 | 6e-24 | 38/45 (A-427, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.425×** | -9.3 | 8e-19 | 36/49 (NCI-H23, LoVo, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.307×** | -9.2 | 9e-19 | 42/48 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.536×** | -8.8 | 5e-17 | 45/48 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.565×** | -8.5 | 4e-16 | 42/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -6.8 | 3e-10 | 30/49 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.678×** | -5.8 | 2e-07 | 37/48 (SW 1271, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.798×** | -4.7 | 5e-05 | 32/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.755×** | -4.2 | 5e-04 | 27/48 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.823×** | -4.1 | 8e-04 | 24/48 (HOP62, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 199 | 0 | 21 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -24.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -21.9) |
| [[PANC-1 (line)]] | alt | 220 | 0 | 19 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -25.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -24.1) |
| [[A-427 (line)]] | wt | 195 | 0 | 15 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -13.2) |
| [[AN3 CA (line)]] | alt | 276 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0902× (z -24.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 160 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -15.3) |
| [[SNU-423 (line)]] | alt | 174 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -23.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -16.8) |
| [[HCT15 (line)]] | alt | 165 | 0 | 14 (8 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.179× (z -15.7) |
| [[HOP62 (line)]] | alt | 161 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -20.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -18.3) |
| [[LoVo (line)]] | wt | 163 | 1 (1 ⚠) | 13 (6 ⚠) | [[Selinexor (drug)]] 5 µM 1.59× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.206× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.268× (z -17.9) |
| [[J82 (line)]] | alt | 87.9 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -19.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -17.6) |
| [[KATO III (line)]] | alt | 98.8 | 0 | 13 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -17.5) |
| [[SW480 (line)]] | alt | 112 | 0 | 13 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.122× (z -23.3) |
| [[A549 (line)]] | wt | 185 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -29.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -16.3) |
| [[C-33 A (line)]] | alt | 299 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0495× (z -30.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 140 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -19.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -13.2) |
| [[C32 (line)]] | wt | 162 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -24.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -18.3) |
| [[H4 (line)]] | wt | 141 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -19.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 125 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -23.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -15.1) |
| [[LOX-IMVI (line)]] | wt | 138 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -17.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.185× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 171 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -21.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -18.4) |
| [[NCI-H23 (line)]] | alt | 226 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -18.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.376× (z -12.5) |
| [[A-172 (line)]] | wt | 97.8 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -18.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -11.4) |
| [[LS 180 (line)]] | wt | 73.2 | 1 (1 ⚠) | 8 (5 ⚠) | [[Selinexor (drug)]] 5 µM 2.10× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 94.7 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -16.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -15.2) |
| [[SNU-1 (line)]] | wt | 125 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -18.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.150× (z -16.2) |
| [[Hs 766T (line)]] | wt | 96.4 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -11.0) |
| [[HS-578T (line)]] | alt | 88.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -17.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -11.0) |
| [[HT-29 (line)]] | alt | 58.7 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 99.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -16.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 85.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -16.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -11.0) |
| [[SHP-77 (line)]] | alt | 61.3 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -13.6) |
| [[SW 900 (line)]] | alt | 103 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 65.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.00× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 133 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.342× (z -9.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 62.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -14.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[COLO 205 (line)]] | alt | 40.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 49.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0848× (z -14.6) ⚠ toxic |
| [[RKO (line)]] | wt | 57.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.289× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 141 | 0 | 2 | — | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM 0.0680× (z -9.4) |
| [[SW48 (line)]] | wt | 82.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0931× (z -15.5) |
| [[BT-474 (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -12.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 102 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 176 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.101× (z -11.2) |
| [[NCI-H2122 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMDS-DT]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[IMMP2L]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TBCK]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BABAM2]] | +0.57 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PNPLA4]] | +0.56 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[LINC01473]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TBC1D5]] | +0.55 | +0.58 / +0.43 | both halves | 4e-05 |  |
| [[DOCK7]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[TRIM66]] | +0.52 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ANKRD26]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[OMA1]] | +0.52 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[STX17]] | +0.51 | +0.56 / +0.47 | both halves | 2e-05 | STRING 674 |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAPGEF3]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ARHGEF1]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CEP295NL]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[GSDMB]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[TMEM243]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[RAB43]] | -0.50 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[PLEKHM1P1]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MAPKAPK2]] | -0.48 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[BLCAP]] | -0.48 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[DPP9]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TMEM104]] | -0.47 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[EHBP1L1]] | -0.46 | -0.38 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers ATG10's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[WWOX]] | B | WWOX activity raises ATG10's level | lines that do not express WWOX (5) vs lines expressing it (45) | 1.59× lower at baseline in the lines without WWOX | 0.053 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ATG10's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRKN]] | B | PRKN activity raises ATG10's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without PRKN | 0.072 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[MAP2K2]] | B | MAP2K2 activity lowers ATG10's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.446). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.1, 30.5); signed map (9.6, -13.0). **Vector** length 80.7, 32.1% of its response variance represented; |z| ≥ 3 in 1,740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.5 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.9 | -13.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.4 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.1 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +4.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -6.9 | -11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -5.1 | -9.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.6 | -10.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -1.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -3.0 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1-q14.2 — chr5:81,972,023-82,276,857 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586I0418, FLJ13954; previously APG10L |
| Gene groups (HGNC) | Autophagy related; Autophagy related E2 enzymes |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0Y0](https://www.uniprot.org/uniprotkb/Q9H0Y0) (Ubiquitin-like-conjugating enzyme ATG10):

> E2-like enzyme involved in autophagy. Acts as an E2-like enzyme that catalyzes the conjugation of ATG12 to ATG5. ATG12 conjugation to ATG5 is required for autophagy. Likely serves as an ATG5-recognition molecule. Not involved in ATG12 conjugation to ATG3 (By similarity). Plays a role in adenovirus-mediated cell lysis.

**Summary**, from NCBI Gene [83734](https://www.ncbi.nlm.nih.gov/gene/83734):

> Autophagy is a process for the bulk degradation of cytosolic compartments by lysosomes. ATG10 is an E2-like enzyme involved in 2 ubiquitin-like modifications essential for autophagosome formation: ATG12 (MIM 609608)-ATG5 (MIM 604261) conjugation and modification of a soluble form of MAP-LC3 (MAP1LC3A; MIM 601242), a homolog of yeast Apg8, to a membrane-bound form (Nemoto et al., 2003 [PubMed 12890687]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20315) · Entrez [83734](https://www.ncbi.nlm.nih.gov/gene/83734) · UniProt [Q9H0Y0](https://www.uniprot.org/uniprotkb/Q9H0Y0) · Ensembl [ENSG00000152348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152348)

## Data

Gene col 7616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7616); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7616]; `tensor/DDL_lfc|DDL_z.npy` [7616]; `embed/gene_vectors.npy` [7616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7616 or target_col == 7616). Every well: [[ATG10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
