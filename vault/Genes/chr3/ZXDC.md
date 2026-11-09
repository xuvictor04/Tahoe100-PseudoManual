---
symbol: "ZXDC"
type: "gene"
col: 952
ensembl_id: "ENSG00000070476"
name: "ZXD family zinc finger C"
location: "3q21.3"
module: 3
arm: "+"
pooled_cpm: 119.64
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ZXDC

*ZXD family zinc finger C* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.34× (z +7.1, q 1e-09, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.472× (z -16.5, q 0e+00, down in 41 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.743× (z -10.0, q 2e-21, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNQ]] (+0.69, fdr 2e-05), [[RPP21]] (+0.66, fdr 1e-05), [[ARID3A]] (+0.63, fdr 1e-05); moves opposite to [[HMGN1]] (-0.64, fdr 1e-05), [[NXT2]] (-0.61, fdr 1e-05), [[ILF3]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SMARCA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +7.1 | 1e-09 | 33/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +5.2 | 6e-05 | 29/48 (NCI-H2030, SW480, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +5.1 | 6e-05 | 32/49 (HT-29, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +4.8 | 2e-04 | 27/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +4.8 | 2e-04 | 25/49 (SW480, NCI-H2347, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.011 | 24/48 (LS 180, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.012 | 15/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.4 | 0.053 | 20/48 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.053 | 17/48 (Hs 766T, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.053 | 20/48 (SW480, HOP62, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.062 | 12/48 (SW1417, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 952.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.472×** | -16.5 | 0e+00 | 41/45 (J82, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.525×** | -15.3 | 0e+00 | 43/49 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.517×** | -15.1 | 0e+00 | 41/44 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.725×** | -10.8 | 5e-25 | 30/48 (LOX-IMVI, SK-MEL-2, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -10.0 | 2e-21 | 34/49 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -9.5 | 2e-19 | 38/47 (NCI-H1792, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.686×** | -8.9 | 3e-17 | 31/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.696×** | -8.6 | 4e-16 | 31/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.786×** | -8.1 | 4e-14 | 31/48 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -7.8 | 3e-13 | 33/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.543×** | -7.6 | 1e-12 | 35/49 (J82, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.549×** | -7.5 | 4e-12 | 29/38 (Panc 03.27, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.745×** | -6.7 | 8e-10 | 31/48 (J82, SK-MEL-2, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.617×** | -6.0 | 8e-08 | 35/48 (SK-MEL-2, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.8 | 5e-05 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.827×** | -4.5 | 2e-04 | 26/48 (NCI-H460, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.887× | -4.0 | 0.002 | 14/48 (A-172, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.843× | -3.9 | 0.003 | 20/48 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.832×** | -3.1 | 0.047 | 13/49 (J82, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elagolix sodium (drug)]] 0.5 µM |  | 0.872× | -3.0 | 0.054 | 15/48 (SW480, HS-578T, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.784×** | -3.0 | 0.054 | 18/49 (NCI-H1573, C-33 A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 330 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -16.7) |
| [[HS-578T (line)]] | alt | 122 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 87.5 | 0 | 9 (8 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.364× (z -15.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.557× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 146 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -16.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 144 | 2 (1 ⚠) | 6 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.71× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -19.8) |
| [[PANC-1 (line)]] | alt | 123 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.395× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 143 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -15.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -17.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -13.3) |
| [[NCI-H1792 (line)]] | alt | 89.4 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -8.6) |
| [[H4 (line)]] | wt | 141 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -9.9) |
| [[A-172 (line)]] | wt | 140 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -15.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -12.8) |
| [[HT-29 (line)]] | alt | 162 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -14.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 90.0 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.361× (z -10.2) ⚠ toxic |
| [[KATO III (line)]] | alt | 158 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.355× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 133 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -17.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 136 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0897× (z -18.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 143 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -16.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -10.3) |
| [[HOP62 (line)]] | alt | 117 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.96× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 173 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -20.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 96.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.3) |
| [[A-427 (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0410× (z -46.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 92.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -8.7) |
| [[A549 (line)]] | wt | 77.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -13.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 95.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -10.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0804× (z -16.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 90.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -19.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 93.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -14.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[C-33 A (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -13.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 99.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -10.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HepG2_C3A (line)]] | wt | 134 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -13.2) |
| [[LS 180 (line)]] | wt | 98.9 | 1 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2347 (line)]] | alt | 80.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.578× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW 1088 (line)]] | alt | 85.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0963× (z -9.0) |
| [[SW1417 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.518× (z -8.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 102 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNQ]] | +0.69 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[RPP21]] | +0.66 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.63 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SELENOS]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MRPL41]] ⚠ | +0.62 | +0.46 / +0.58 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDC34]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PPFIA1]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ALG2]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[POLR2J4]] | +0.61 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[KXD1]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CIAO2B]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TBC1D20]] | +0.60 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[MPG]] | +0.60 | +0.40 / +0.59 | both halves | 5e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN1]] | -0.64 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[NXT2]] | -0.61 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[ILF3]] | -0.59 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SH3BGRL]] | -0.58 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[HFE]] | -0.58 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ZNF300]] | -0.57 | -0.42 / -0.47 | both halves | 4e-05 | same gene group |
| [[GBA1]] | -0.57 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[GALC]] | -0.56 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[PFKM]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[HMGN2]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SUMO3]] | -0.56 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[HNRNPM]] | -0.55 | -0.40 / -0.57 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMARCA1]] | B | SMARCA1 activity raises ZXDC's level | lines that do not express SMARCA1 (13) vs lines expressing it (37) | 1.10× lower at baseline in the lines without SMARCA1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TGFBR2; also absent: ENSG00000268163, ZNF772, SNRPN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.7, -14.9); signed map (-29.4, 13.0). **Vector** length 122, 36.9% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +5.6 | +4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +7.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.3 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.0 | +3.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -11.3 | -15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -11.3 | -16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -10.7 | -15.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -10.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.0 | -8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -6.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ZXD family zinc finger C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:126,437,601-126,475,891 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11349, FLJ13861 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2QGD7](https://www.uniprot.org/uniprotkb/Q2QGD7) (Zinc finger protein ZXDC):

> Cooperates with CIITA to promote transcription of MHC class I and MHC class II genes.

**Summary**, from NCBI Gene [79364](https://www.ncbi.nlm.nih.gov/gene/79364):

> Enables C2H2 zinc finger domain binding activity; LRR domain binding activity; and transcription coactivator activity. Involved in positive regulation of DNA-templated transcription. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28160) · Entrez [79364](https://www.ncbi.nlm.nih.gov/gene/79364) · UniProt [Q2QGD7](https://www.uniprot.org/uniprotkb/Q2QGD7) · Ensembl [ENSG00000070476](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070476)

## Data

Gene col 952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 952); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 952]; `tensor/DDL_lfc|DDL_z.npy` [952]; `embed/gene_vectors.npy` [952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 952 or target_col == 952). Every well: [[ZXDC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZXDC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
