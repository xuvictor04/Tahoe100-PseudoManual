---
symbol: "SUMO3"
type: "gene"
col: 11588
ensembl_id: "ENSG00000184900"
name: "small ubiquitin like modifier 3"
location: "21q22.3"
module: 29
arm: "+"
pooled_cpm: 21.98
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SUMO3

*small ubiquitin like modifier 3* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.02× (z +21.7, q 0e+00, up in 37 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +5.8, q 8e-07, up in 26 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 6.81×, HEC-1-A 6.03×, HOP62 6.59×, MIA PaCa-2 7.89×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 5.86×, HOP62 5.73×, MIA PaCa-2 8.20×, PANC-1 8.29×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.69×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.575× (z -9.5, q 2e-18, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUCA2]] (+0.77, fdr 7e-06), [[PGRMC1]] (+0.74, fdr 7e-06), [[MOB1A]] (+0.73, fdr 7e-06); moves opposite to [[UBE2B]] (-0.66, fdr 1e-05), [[RBMX2]] (-0.65, fdr 7e-06), [[ARID3A]] (-0.64, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[APPAT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11588.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 6.81×, HEC-1-A 6.03×, HOP62 6.59×, MIA PaCa-2 7.89×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 5.86×, HOP62 5.73×, MIA PaCa-2 8.20×, PANC-1 8.29×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.69×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.02×** | +21.7 | 0e+00 | 37/37 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.14×** | +19.0 | 0e+00 | 31/31 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.45×** | +13.8 | 4e-41 | 35/35 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.8 | 8e-07 | 26/45 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.53×** | +5.1 | 3e-05 | 28/44 (HOP62, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.52×** | +4.9 | 1e-04 | 27/44 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.5 | 4e-04 | 25/47 (A-172, CFPAC-1, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.44×** | +4.2 | 0.002 | 26/47 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.2 | 0.078 | 11/32 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.575×** | -9.5 | 2e-18 | 30/46 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.506×** | -8.2 | 6e-14 | 39/47 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.539×** | -7.5 | 2e-11 | 33/45 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.549×** | -7.3 | 6e-11 | 41/47 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.567×** | -6.9 | 8e-10 | 40/47 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -6.3 | 2e-08 | 31/45 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.596×** | -6.3 | 3e-08 | 35/47 (SW480, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.497×** | -4.4 | 7e-04 | 28/47 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 0.618× | -3.0 | 0.14 | 19/45 (MIA PaCa-2, RPMI-7951, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.1 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 6.81× (z +17.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 7.89× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0737× (z -17.1) |
| [[CFPAC-1 (line)]] | alt | 39.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -8.5) |
| [[HOP62 (line)]] | alt | 33.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +15.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 52.8 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +12.0) | — |
| [[A498 (line)]] | wt | 21.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 21.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 44.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.03× (z +16.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 21.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.78× (z +12.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 19.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.84× (z +12.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 21.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.29× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 33.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 13.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.44× (z +13.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 12.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.85× (z +13.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 26.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.08× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 13.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 19.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +11.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 14.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.05× (z +12.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 26.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 18.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 13.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.60× (z +11.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 31.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +12.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.73× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 19.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.10× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 9.11 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.9× (z +11.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 12.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.54× (z +9.5) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.83× (z +9.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +10.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 15.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.05× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -11.0) |
| [[RKO (line)]] | wt | 12.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.141× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 19.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.19× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -12.5) |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUCA2]] | +0.77 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[PGRMC1]] | +0.74 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.73 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[HCFC1]] | +0.71 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[CYB561A3]] | +0.68 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[CTSZ]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[BANF1]] | +0.68 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[NCSTN]] | +0.67 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[C5orf15]] | +0.66 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[RCN1]] | +0.66 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[CDK2AP1]] | +0.66 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CNOT1]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2B]] | -0.66 | -0.60 / -0.55 | both halves | 1e-05 | STRING 415 |
| [[RBMX2]] | -0.65 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[ARID3A]] | -0.64 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[MPHOSPH10]] | -0.63 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[EIF5B]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[MTRES1]] | -0.63 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.63 | -0.66 / -0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CCDC112]] | -0.63 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ATF4]] | -0.63 | -0.58 / -0.67 | both halves | 7e-06 | STRING 433 |
| [[CROCCP2-1]] | -0.62 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[NOL7]] ⚠ | -0.62 | -0.38 / -0.58 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RP9]] | -0.62 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[CINP]] | -0.61 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[MARCHF9]] | -0.61 | -0.63 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APPAT]] | B | APPAT activity lowers SUMO3's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.48× higher at baseline in the lines without APPAT | 0.032 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SUMO3's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises SUMO3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[A1BG-AS1]] | B | A1BG-AS1 activity lowers SUMO3's level | lines that do not express A1BG-AS1 (18) vs lines expressing it (32) | 1.10× higher at baseline in the lines without A1BG-AS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: A1BG, DZIP1, RNF150 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-27.5, -21.4); signed map (-21.1, -38.7). **Vector** length 77.1, 16.6% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +19.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +21.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +0.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -6.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | -7.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.6 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | small ubiquitin like modifier 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:44,805,617-44,818,779 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMT3A; previously SMT3H1 |
| Gene groups (HGNC) | Small ubiquitin like modifier family |
| Reactome | 17 pathways, smallest: SUMO is conjugated to E1 (UBA2:SAE1); SUMO is proteolytically processed; SUMO is transferred from E1 to E2 (UBE2I, UBC9) |
| Matched by | ensembl_id |

**Function**, from UniProt [P55854](https://www.uniprot.org/uniprotkb/P55854) (Small ubiquitin-related modifier 3):

> Ubiquitin-like protein which can be covalently attached to target lysines either as a monomer or as a lysine-linked polymer. Does not seem to be involved in protein degradation and may function as an antagonist of ubiquitin in the degradation process. Plays a role in a number of cellular processes such as nuclear transport, DNA replication and repair, mitosis and signal transduction. Covalent attachment to its substrates requires prior activation by the E1 complex SAE1-SAE2 and linkage to the …

**Summary**, from NCBI Gene [6612](https://www.ncbi.nlm.nih.gov/gene/6612):

> This gene encodes a member of the small ubiquitin-related modifier (SUMO) family of eukaryotic proteins. The encoded protein is covalently conjugated to other proteins via a post-translation modification known as sumoylation. Sumoylation may play a role in a wide variety of cellular processes, including nuclear transport, DNA replication and repair, mitosis, transcriptional regulation, and signal transduction. Alternatively spliced transcript variants encoding distinct proteins have been …

**Accessions** — [HGNC:11124](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11124) · Entrez [6612](https://www.ncbi.nlm.nih.gov/gene/6612) · UniProt [P55854](https://www.uniprot.org/uniprotkb/P55854) · Ensembl [ENSG00000184900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184900)

## Data

Gene col 11588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11588); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11588]; `tensor/DDL_lfc|DDL_z.npy` [11588]; `embed/gene_vectors.npy` [11588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11588 or target_col == 11588). Every well: [[SUMO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUMO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
