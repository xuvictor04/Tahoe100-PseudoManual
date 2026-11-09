---
symbol: "POLE2"
type: "gene"
col: 1970
ensembl_id: "ENSG00000100479"
name: "DNA polymerase epsilon 2, accessory subunit"
location: "14q21.3"
module: 6
arm: "+"
pooled_cpm: 17.99
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# POLE2

*DNA polymerase epsilon 2, accessory subunit* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.25× (z +16.7, q 0e+00, up in 21 of 25 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 1.19× (z +3.6, q 0.012, up in 10 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.668× (z -8.4, q 1e-14, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX12P]] (+0.81, fdr 7e-06), [[FANCI]] (+0.81, fdr 7e-06), [[RFC4]] (+0.80, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDCA7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.25×** | +16.7 | 0e+00 | 21/25 (SHP-77, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.85×** | +15.4 | 0e+00 | 32/38 (SHP-77, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.58×** | +12.9 | 7e-36 | 20/35 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.57×** | +6.6 | 5e-09 | 21/47 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.51×** | +6.0 | 2e-07 | 23/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +5.5 | 3e-06 | 21/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.46×** | +5.4 | 7e-06 | 17/43 (NCI-H460, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **1.45×** | +5.2 | 1e-05 | 18/41 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +5.1 | 3e-05 | 19/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.38×** | +4.7 | 1e-04 | 16/46 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.35×** | +4.4 | 4e-04 | 17/47 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.35×** | +4.4 | 6e-04 | 15/47 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.31×** | +4.0 | 0.003 | 14/47 (PANC-1, A-427, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.6 | 0.012 | 10/48 (PANC-1, CHP-212, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.028 | 8/47 (HepG2/C3A, J82, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.045 | 5/48 (PANC-1, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.069 | 8/48 (C-33 A, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1970.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.668×** | -8.4 | 1e-14 | 26/47 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.566×** | -8.4 | 1e-14 | 28/46 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.572×** | -7.9 | 4e-13 | 26/46 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.596×** | -7.6 | 4e-12 | 28/47 (SW48, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.787×** | -5.0 | 7e-05 | 18/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.531×** | -4.9 | 1e-04 | 21/48 (A-427, HCT15, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.725×** | -4.7 | 2e-04 | 19/46 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.798×** | -4.7 | 2e-04 | 17/48 (RKO, COLO 205, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.574×** | -4.3 | 0.001 | 20/44 (NCI-H2030, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.830×** | -3.9 | 0.006 | 11/48 (A-427, COLO 205, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.769×** | -3.9 | 0.006 | 13/47 (SK-MEL-2, HOP62, …) | two highest doses | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.763×** | -3.8 | 0.008 | 15/48 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.649×** | -3.3 | 0.036 | 15/45 (SW48, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.729×** | -3.3 | 0.036 | 16/48 (SW480, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **0.792×** | -3.3 | 0.036 | 13/47 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.809×** | -3.1 | 0.061 | 9/47 (C32, HOP62, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.811×** | -3.1 | 0.063 | 10/48 (RKO, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.865× | -3.0 | 0.071 | 18/48 (A498, A-427, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.815×** | -3.0 | 0.071 | 13/47 (NCI-H23, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.818×** | -3.0 | 0.081 | 17/47 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.74 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 41.2 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.100× (z -18.4) |
| [[A498 (line)]] | wt | 15.2 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 41.1 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0973× (z -14.1) |
| [[HOP62 (line)]] | alt | 11.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.4× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H23 (line)]] | alt | 30.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -13.6) |
| [[SW48 (line)]] | wt | 30.2 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.117× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 12.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.82× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0668× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 8.55 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.63× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0959× (z -9.5) |
| [[J82 (line)]] | alt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 38.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.215× (z -11.4) |
| [[PANC-1 (line)]] | alt | 25.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.2) |
| [[SHP-77 (line)]] | alt | 47.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.25× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.1) |
| [[C-33 A (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0576× (z -9.1) |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.107× (z -8.8) |
| [[LoVo (line)]] | wt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.232× (z -9.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H460 (line)]] | wt | 11.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.09× (z +9.5) ⚠ toxic; cell-cycle shift, explains ~51% of this change | — |
| [[SW 900 (line)]] | alt | 7.28 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0745× (z -9.4) |
| [[A-172 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX12P]] | +0.81 | +0.80 / +0.78 | both halves | 7e-06 |  |
| [[FANCI]] | +0.81 | +0.81 / +0.76 | both halves | 7e-06 | STRING 486 |
| [[RFC4]] | +0.80 | +0.79 / +0.80 | both halves | 7e-06 | pathway: Base Excision Repair; STRING 935 |
| [[DSCC1]] | +0.80 | +0.78 / +0.82 | both halves | 7e-06 | STRING 610 |
| [[RAD51]] | +0.80 | +0.81 / +0.76 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 788 |
| [[CENPK]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[DDX11]] | +0.80 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[WDR76]] | +0.79 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[FANCA]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[EXO1]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 866 |
| [[MSH2]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 | STRING 579 |
| [[CDC45]] | +0.77 | +0.76 / +0.77 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7]] | B | CDCA7 activity raises POLE2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.19× lower at baseline in the lines without CDCA7 | 0.047 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.794). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.0, -45.4); signed map (-37.1, -43.0). **Vector** length 118, 30.9% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.58 to 65); *DNA strand elongation* (reactome, mean cos +0.62 to 28); *E2F G1/S* (control, mean cos +0.59 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +5.0 | +15.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | +5.0 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.9 | +16.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.2 | +4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +2.4 | +3.2 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.4 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.7 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.2 | -5.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase epsilon 2, accessory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:49,643,555-49,688,422 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DPE2 |
| Gene groups (HGNC) | DNA polymerases |
| Reactome | 30 pathways, smallest: DNA replication initiation; PCNA-Dependent Long Patch Base Excision Repair; Gap-filling DNA repair synthesis and ligation in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [P56282](https://www.uniprot.org/uniprotkb/P56282) (DNA polymerase epsilon subunit 2):

> Accessory component of the DNA polymerase epsilon complex. Participates in DNA repair and in chromosomal DNA replication (By similarity).

**Summary**, from NCBI Gene [5427](https://www.ncbi.nlm.nih.gov/gene/5427):

> DNA polymerase epsilon, which is involved in DNA repair and replication, is composed of a large catalytic subunit and a small accessory subunit. The protein encoded by this gene represents the small subunit (B). Defects in this gene have been linked to colorectal cancer and to combined immunodeficiency. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:9178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9178) · Entrez [5427](https://www.ncbi.nlm.nih.gov/gene/5427) · UniProt [P56282](https://www.uniprot.org/uniprotkb/P56282) · Ensembl [ENSG00000100479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100479)

## Data

Gene col 1970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1970); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1970]; `tensor/DDL_lfc|DDL_z.npy` [1970]; `embed/gene_vectors.npy` [1970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1970 or target_col == 1970). Every well: [[POLE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
