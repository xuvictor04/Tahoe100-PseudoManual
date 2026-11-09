---
symbol: "GMDS-DT"
type: "gene"
col: 14718
ensembl_id: "ENSG00000250903"
name: "GMDS divergent transcript"
location: "6p25.3-p25.2"
module: 10
arm: "+"
pooled_cpm: 140.1
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 45
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# GMDS-DT

*GMDS divergent transcript* — 6p25.3-p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.44× (z +4.4, q 0.007, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (24 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.231× (z -17.9, q 0e+00, down in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.307× (z -14.5, q 4e-45, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATG10]] (+0.63, fdr 7e-06), [[LINC01473]] (+0.62, fdr 7e-06), [[FSIP2-AS1]] (+0.61, fdr 1e-05); moves opposite to [[CEP295NL]] (-0.55, fdr 1e-05), [[LLGL1]] (-0.55, fdr 3e-05), [[LPCAT4]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +4.4 | 0.007 | 30/47 (AsPC-1, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.026 | 33/47 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.032 | 32/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.043 | 26/49 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.043 | 24/48 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.054 | 28/48 (SW48, SW480, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.21× | +3.2 | 0.10 | 23/48 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.33× | +3.2 | 0.10 | 26/50 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.63× | +3.2 | 0.10 | 25/50 (NCI-H23, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 24 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14718.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.231×** | -17.9 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.239×** | -17.5 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.307×** | -14.5 | 4e-45 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.373×** | -12.1 | 2e-31 | 47/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.378×** | -11.9 | 1e-30 | 47/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.364×** | -11.9 | 1e-30 | 43/47 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.178×** | -11.1 | 2e-26 | 46/48 (MIA PaCa-2, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.534×** | -10.8 | 2e-25 | 34/48 (C32, NCI-H1792, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.188×** | -10.7 | 6e-25 | 48/49 (COLO 205, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.417×** | -10.3 | 5e-23 | 39/48 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.447×** | -9.5 | 1e-19 | 42/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.502×** | -8.4 | 2e-15 | 43/48 (PANC-1, HCT15, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -7.9 | 9e-14 | 44/49 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.555×** | -6.8 | 5e-10 | 41/48 (HT-29, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.579×** | -6.7 | 1e-09 | 42/48 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.628×** | -5.7 | 4e-07 | 39/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.785×** | -4.1 | 7e-04 | 28/48 (A-172, J82, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.730×** | -3.8 | 0.003 | 33/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.821×** | -3.4 | 0.013 | 26/49 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.610×** | -3.2 | 0.027 | 26/48 (LOX-IMVI, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.831×** | -3.2 | 0.027 | 23/49 (LoVo, NCI-H23, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.697×** | -3.1 | 0.027 | 26/49 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 125 | 0 | 19 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -21.1) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.184× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 216 | 0 | 18 (13 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0738× (z -29.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.277× (z -15.3) |
| [[SW480 (line)]] | alt | 218 | 0 | 16 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.145× (z -20.5) |
| [[HEC-1-A (line)]] | alt | 208 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -20.3) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0955× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 225 | 0 | 15 (8 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0607× (z -14.9) |
| [[C32 (line)]] | wt | 150 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -23.9) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.264× (z -11.4) |
| [[LoVo (line)]] | wt | 193 | 0 | 14 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.265× (z -15.3) |
| [[HT-29 (line)]] | alt | 226 | 0 | 13 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.274× (z -13.1) |
| [[KATO III (line)]] | alt | 263 | 0 | 13 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0947× (z -12.6) |
| [[PANC-1 (line)]] | alt | 116 | 0 | 13 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -20.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.153× (z -18.6) |
| [[J82 (line)]] | alt | 92.7 | 0 | 12 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -17.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.220× (z -13.8) |
| [[A-427 (line)]] | wt | 109 | 0 | 10 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.303× (z -12.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.176× (z -9.9) |
| [[HCT15 (line)]] | alt | 150 | 0 | 10 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -17.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.192× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 155 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -14.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.129× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 176 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -21.8) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.320× (z -10.3) |
| [[A549 (line)]] | wt | 123 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -19.1) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -9.6) |
| [[C-33 A (line)]] | alt | 162 | 0 | 9 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0329× (z -27.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.314× (z -9.8) |
| [[LS 180 (line)]] | wt | 167 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -16.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.168× (z -14.3) |
| [[SNU-423 (line)]] | alt | 106 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -13.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.273× (z -10.4) |
| [[COLO 205 (line)]] | alt | 380 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.229× (z -15.5) |
| [[HS-578T (line)]] | alt | 79.7 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.8) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.183× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 84.2 | 0 | 8 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -15.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.249× (z -10.5) |
| [[BT-474 (line)]] | alt | 144 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.224× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 64.6 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.270× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 148 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0974× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.110× (z -11.7) |
| [[SNU-1 (line)]] | wt | 143 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -13.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.194× (z -12.8) |
| [[A-172 (line)]] | wt | 124 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 6 (3 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0911× (z -11.0) |
| [[H4 (line)]] | wt | 82.8 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -18.6) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.156× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.300× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 228 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.250× (z -12.8) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.327× (z -10.8) |
| [[HOP62 (line)]] | alt | 98.2 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.238× (z -11.6) |
| [[Hs 766T (line)]] | wt | 135 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.266× (z -10.5) |
| [[RKO (line)]] | wt | 137 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.171× (z -14.1) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.100× (z -10.0) |
| [[SHP-77 (line)]] | alt | 93.2 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.202× (z -12.8) |
| [[SW1417 (line)]] | alt | 92.4 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.231× (z -11.9) |
| [[A498 (line)]] | wt | 93.0 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.168× (z -13.5) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 145 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0781× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.149× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 94.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.4) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SW 1088 (line)]] | alt | 148 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0559× (z -10.9) |
| [[SW 1271 (line)]] | alt | 235 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -11.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 82.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.134× (z -11.5) |
| [[CHP-212 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -14.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG10]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[LINC01473]] | +0.62 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[FSIP2-AS1]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[STX17]] | +0.60 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[PUDP]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[R3HDM2]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[OMA1]] | +0.58 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[PRH1]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[PRR4]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[SLC38A4-AS1]] | +0.56 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[LINC02340]] | +0.56 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SUMF1]] | +0.55 | +0.64 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP295NL]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[LLGL1]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[LPCAT4]] | -0.52 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[MMP15]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[TIMP2]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[PTK7]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CDR2L]] | -0.48 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[ANKRD13D]] | -0.48 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[RAB43]] | -0.47 | -0.49 / -0.29 | both halves | 2e-04 |  |
| [[MCUB]] | -0.47 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[AP1S1]] | -0.47 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[EPHB4]] | -0.46 | -0.60 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises GMDS-DT's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without FSIP2-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises GMDS-DT's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.413). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-24.5, 31.7); signed map (9.1, -12.7). **Vector** length 75.7, 30.5% of its response variance represented; |z| ≥ 3 in 1,754 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.9 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.6 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.5 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +4.1 | -10.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.3 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.2 | -9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.8 | -3.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -3.7 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -1.0 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.7 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | GMDS divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p25.3-p25.2 — chr6:2,245,718-2,525,976 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously GMDS-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48993) · Entrez [100508120](https://www.ncbi.nlm.nih.gov/gene/100508120) · Ensembl [ENSG00000250903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250903)

## Data

Gene col 14718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14718); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14718]; `tensor/DDL_lfc|DDL_z.npy` [14718]; `embed/gene_vectors.npy` [14718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14718 or target_col == 14718). Every well: [[GMDS-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMDS-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
