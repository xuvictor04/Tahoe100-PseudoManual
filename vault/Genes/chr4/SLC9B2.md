---
symbol: "SLC9B2"
type: "gene"
col: 8840
ensembl_id: "ENSG00000164038"
name: "solute carrier family 9 member B2"
location: "4q24"
module: 5
arm: "+"
pooled_cpm: 22.98
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SLC9B2

*solute carrier family 9 member B2* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.51× (z +9.4, q 2e-18, up in 28 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.33× (z +6.8, q 2e-09, up in 18 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.366× (z -23.9, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDDC2]] (+0.65, fdr 3e-05), [[EEF1AKMT1]] (+0.64, fdr 1e-05), [[NSMAF]] (+0.63, fdr 1e-05); moves opposite to [[RASSF7]] (-0.55, fdr 4e-05), [[DCTN3]] (-0.55, fdr 4e-05), [[PLAG1]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ULK2]] → it (grade B ⚠); 7 go from it, the strongest it → [[QTRT1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8840.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +9.4 | 2e-18 | 28/43 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +8.6 | 2e-15 | 22/35 (HS-578T, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +7.6 | 4e-12 | 16/30 (SHP-77, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +6.8 | 2e-09 | 18/44 (NCI-H2347, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +6.0 | 3e-07 | 15/45 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.9 | 8e-05 | 15/39 (SW 900, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.2 | 0.003 | 6/28 (A-427, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.19× | +4.0 | 0.004 | 6/44 (AsPC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +4.0 | 0.004 | 6/45 (H4, SK-MEL-2, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.020 | 9/45 (NCI-H460, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | 1.11× | +3.5 | 0.020 | 11/45 (NCI-H2347, KATO III, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.16× | +3.5 | 0.023 | 10/45 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.036 | 8/44 (Panc 03.27, C-33 A, …) | inconsistent across doses |  |
| [[Gallic acid (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.037 | 3/44 (MIA PaCa-2, HCT15, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.15× | +3.2 | 0.051 | 4/44 (BT-474, AsPC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.067 | 8/44 (SNU-423, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.366×** | -23.9 | 0e+00 | 37/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.433×** | -19.9 | 0e+00 | 35/45 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.535×** | -14.8 | 0e+00 | 34/45 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.635×** | -10.8 | 7e-25 | 28/45 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.670×** | -9.5 | 3e-19 | 27/43 (PANC-1, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.696×** | -8.6 | 8e-16 | 27/45 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.747×** | -6.9 | 4e-10 | 19/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.800×** | -5.1 | 3e-05 | 18/45 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **0.809×** | -5.0 | 3e-05 | 19/42 (A498, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.817×** | -4.8 | 1e-04 | 18/44 (NCI-H460, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.824×** | -4.6 | 2e-04 | 16/45 (NCI-H460, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.714×** | -4.2 | 0.001 | 13/45 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.889× | -3.9 | 0.004 | 19/45 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.848× | -3.9 | 0.004 | 16/45 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.849× | -3.9 | 0.004 | 16/45 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.895× | -3.7 | 0.007 | 6/45 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.854× | -3.6 | 0.011 | 12/43 (LS 180, NCI-H2030, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.865× | -3.4 | 0.020 | 9/45 (NCI-H1573, CFPAC-1, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.874× | -3.2 | 0.042 | 10/45 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.876× | -3.1 | 0.048 | 11/45 (A-427, KATO III, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.880× | -3.0 | 0.062 | 5/45 (H4, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.881× | -3.0 | 0.065 | 9/45 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.0 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -15.3) |
| [[RKO (line)]] | wt | 68.3 | 0 | 9 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.204× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 34.9 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.299× (z -14.6) |
| [[C-33 A (line)]] | alt | 66.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 55.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 49.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.359× (z -10.4) |
| [[SNU-1 (line)]] | wt | 28.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Brivudine (drug)]] 5 µM 0.0547× (z -8.5) |
| [[SW480 (line)]] | alt | 16.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.263× (z -12.8) |
| [[A-172 (line)]] | wt | 26.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.312× (z -9.1) |
| [[A-427 (line)]] | wt | 36.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -9.3) |
| [[A549 (line)]] | wt | 18.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -11.3) |
| [[LoVo (line)]] | wt | 21.5 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.207× (z -9.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.346× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 54.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -10.8) |
| [[A498 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.310× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~46% of this change |
| [[AN3 CA (line)]] | alt | 43.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -9.7) |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.299× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~46% of this change |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.132× (z -11.2) |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.303× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~75% of this change |
| [[AsPC-1 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDDC2]] | +0.65 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[EEF1AKMT1]] | +0.64 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NSMAF]] | +0.63 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ZNF124]] | +0.63 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[METTL8]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[EPM2A]] | +0.60 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[USP45]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[USP46]] | +0.59 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[GABPB1]] | +0.59 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[DIMT1]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SETMAR]] | +0.59 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[DDX31]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASSF7]] | -0.55 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[DCTN3]] | -0.55 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PLAG1]] | -0.54 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[PJA2]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SRSF9]] ⚠ | -0.53 | -0.45 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DNAAF3]] | -0.51 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[DNM2]] | -0.51 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[SLC17A7]] | -0.50 | -0.51 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ULK2]] | B | ULK2 activity raises SLC9B2's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.96× lower at baseline in the lines without ULK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[SLC17A7]] | B | SLC17A7 activity raises SLC9B2's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 2.05× lower at baseline in the lines without SLC17A7 | 0.031 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[SLC17A7]] | B | SLC17A7 activity strengthens SLC9B2's drug response | lines that do not express SLC17A7 (8) vs lines expressing it (37) | the lines without SLC17A7 respond 0.53× as strongly (z diff +2.01); strongest at Panobinostat 5 µM: 0.76x vs 0.36x (z diff +5.3) | 0.063 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MEX3A]] | B | MEX3A activity raises SLC9B2's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without MEX3A | 0.083 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[QTRT1]] | C | SLC9B2 activity raises QTRT1's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.58× lower at baseline in the lines without SLC9B2 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent; its own permutation p |
| [[NOL9]] | C | SLC9B2 activity raises NOL9's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.31× lower at baseline in the lines without SLC9B2 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent |
| [[VRK2]] | C | SLC9B2 activity raises VRK2's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.33× lower at baseline in the lines without SLC9B2 | 0.087 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent |
| [[MTARC1]] | C | SLC9B2 activity raises MTARC1's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 2.26× lower at baseline in the lines without SLC9B2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent; its own permutation p |
| [[STARD7-AS1]] | C | SLC9B2 activity raises STARD7-AS1's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.40× lower at baseline in the lines without SLC9B2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent; its own permutation p |
| [[UTP20]] | C | SLC9B2 activity raises UTP20's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.39× lower at baseline in the lines without SLC9B2 | 0.098 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent |
| [[WDR12]] | C | SLC9B2 activity raises WDR12's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.38× lower at baseline in the lines without SLC9B2 | 0.099 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.558). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-9.3, 13.1); signed map (12.1, -43.9). **Vector** length 91.1, 18.5% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.8 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.4 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +4.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +7.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -19.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -14.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.7 | -23.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -2.6 | -9.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.4 | -10.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Ixazomib (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 9 member B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:103,019,868-103,085,829 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23984, NHA2; previously NHEDC2 |
| Gene groups (HGNC) | Solute carrier family 9 |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UD5](https://www.uniprot.org/uniprotkb/Q86UD5) (Sodium/hydrogen exchanger 9B2):

> Electroneutral Na(+) Li(+)/H(+) antiporter that extrudes Na(+) or Li(+) in exchange for external protons across the membrane. Uses the proton gradient/membrane potential to extrude sodium. Contributes to the regulation of intracellular pH and sodium homeostasis (By similarity). Also able to mediate Na(+)/Li(+) antiporter activity in kidney. May play a physiological role in renal tubular function and blood pressure homeostasis (By similarity). Plays an important role for insulin secretion and …

**Summary**, from NCBI Gene [133308](https://www.ncbi.nlm.nih.gov/gene/133308):

> Sodium hydrogen antiporters, such as NHEDC2, convert the proton motive force established by the respiratory chain or the F1F0 mitochondrial ATPase into sodium gradients that drive other energy-requiring processes, transduce environmental signals into cell responses, or function in drug efflux (Xiang et al., 2007 [PubMed 18000046]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25143) · Entrez [133308](https://www.ncbi.nlm.nih.gov/gene/133308) · UniProt [Q86UD5](https://www.uniprot.org/uniprotkb/Q86UD5) · Ensembl [ENSG00000164038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164038)

## Data

Gene col 8840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8840); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8840]; `tensor/DDL_lfc|DDL_z.npy` [8840]; `embed/gene_vectors.npy` [8840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8840 or target_col == 8840). Every well: [[SLC9B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
