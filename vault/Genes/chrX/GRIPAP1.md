---
symbol: "GRIPAP1"
type: "gene"
col: 891
ensembl_id: "ENSG00000068400"
name: "GRIP1 associated protein 1"
location: "Xp11.23"
module: 96
arm: "+"
pooled_cpm: 53.63
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# GRIPAP1

*GRIP1 associated protein 1* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.47× (z +12.0, q 2e-30, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.818× (z -15.1, q 0e+00, down in 35 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.552× (z -6.8, q 1e-09, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFE3]] (+0.69, fdr 7e-06, ⚠ same locus), [[CHMP4A]] (+0.66, fdr 7e-06), [[OCIAD1]] (+0.61, fdr 7e-06), [[UPF3B]] (+0.60, fdr 1e-05); moves opposite to [[NME2]] (-0.61, fdr 9e-06), [[DEXI]] (-0.58, fdr 1e-05), [[RNF4]] (-0.57, fdr 9e-06).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ARAF]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +12.0 | 2e-30 | 37/48 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +11.9 | 3e-30 | 37/41 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +11.6 | 6e-29 | 35/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +7.2 | 7e-11 | 29/48 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +7.0 | 2e-10 | 36/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +6.4 | 1e-08 | 28/45 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +6.3 | 2e-08 | 27/48 (SW480, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.7 | 8e-07 | 24/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.14× | +4.2 | 0.001 | 12/48 (A498, LS 180, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.2 | 0.001 | 16/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 0.001 | 18/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.002 | 18/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.18× | +3.6 | 0.015 | 9/48 (A-427, HCT15, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.031 | 9/48 (PANC-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.3 | 0.031 | 18/48 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tolcapone (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.043 | 8/49 (SW480, NCI-H1573, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.818×** | -15.1 | 0e+00 | 35/49 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.723×** | -7.1 | 4e-10 | 28/47 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.552×** | -6.8 | 1e-09 | 32/49 (NCI-H23, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.553×** | -6.8 | 1e-09 | 36/48 (SNU-1, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -6.6 | 4e-09 | 28/48 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.757×** | -6.1 | 1e-07 | 31/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.781×** | -5.3 | 1e-05 | 28/48 (C-33 A, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.793×** | -5.1 | 3e-05 | 18/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -4.6 | 2e-04 | 21/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.817×** | -4.4 | 6e-04 | 21/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **0.814×** | -4.4 | 6e-04 | 25/48 (C-33 A, COLO 205, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.809×** | -3.8 | 0.008 | 15/47 (SW1417, AN3 CA, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.862× | -3.1 | 0.072 | 12/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 61.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.7) | — |
| [[SW480 (line)]] | alt | 94.9 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.477× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.511× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 45.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +12.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 51.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.64× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 21.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 22.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 60.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 25.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 59.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -11.3) |
| [[PANC-1 (line)]] | alt | 65.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -8.6) |
| [[SHP-77 (line)]] | alt | 41.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.26× (z +9.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.360× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 49.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.9) | [[PH-797804 (drug)]] 5 µM 0.0947× (z -9.2) |
| [[A-172 (line)]] | wt | 48.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.4) | — |
| [[A498 (line)]] | wt | 26.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +9.1) | — |
| [[A549 (line)]] | wt | 59.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -10.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 50.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0829× (z -13.1) |
| [[NCI-H661 (line)]] | alt | 36.1 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.0659× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 71.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.221× (z -9.0) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFE3]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 | STRING 612; ⚠ same locus (26.5 kb, same strand: neighbours can correlate without regulation) |
| [[CHMP4A]] | +0.66 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[OCIAD1]] | +0.61 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[UPF3B]] | +0.60 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[STX4]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[MBD6]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CREB3]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ACIN1]] | +0.57 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[EXOC3]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[LARP7]] | +0.55 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TRMT10B]] | +0.55 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[KPNA5]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[KIF3B]] | +0.54 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME2]] | -0.61 | -0.69 / -0.57 | both halves | 9e-06 |  |
| [[DEXI]] | -0.58 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[RNF4]] | -0.57 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[NDC1]] | -0.56 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[ANKRD16]] | -0.56 | -0.22 / -0.64 | both halves | 6e-04 |  |
| [[MFSD14CP]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TSPO]] | -0.54 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[PRDX4]] | -0.53 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[FOXK2]] | -0.53 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TBC1D4]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[HACD3]] | -0.52 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[POM121]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GRIPAP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARAF]] | C | GRIPAP1's natural level strengthens ARAF's drug response | GRIPAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.11; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-25.6, 9.1); signed map (9.7, -19.5). **Vector** length 100, 23.2% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.2 | +3.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Oxaliplatin (drug)]] 0.05 µM |  | +1.6 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | +1.0 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | GRIP1 associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,973,720-49,002,265 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRASP-1, GRASP1, KIAA1167, MPMGp800B12492Q3, DKFZp434P0630 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4V328](https://www.uniprot.org/uniprotkb/Q4V328) (GRIP1-associated protein 1):

> Regulates the endosomal recycling back to the neuronal plasma membrane, possibly by connecting early and late recycling endosomal domains and promoting segregation of recycling endosomes from early endosomal membranes. Involved in the localization of recycling endosomes to dendritic spines, thereby playing a role in the maintenance of dendritic spine morphology. Required for the activity-induced AMPA receptor recycling to dendrite membranes and for long-term potentiation and synaptic plasticity …

**Summary**, from NCBI Gene [56850](https://www.ncbi.nlm.nih.gov/gene/56850):

> This gene encodes a guanine nucleotide exchange factor for the Ras family of small G proteins (RasGEF). The encoded protein interacts in a complex with glutamate receptor interacting protein 1 (GRIP1) and plays a role in the regulation of AMPA receptor function. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:18706](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18706) · Entrez [56850](https://www.ncbi.nlm.nih.gov/gene/56850) · UniProt [Q4V328](https://www.uniprot.org/uniprotkb/Q4V328) · Ensembl [ENSG00000068400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068400)

## Data

Gene col 891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 891); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 891]; `tensor/DDL_lfc|DDL_z.npy` [891]; `embed/gene_vectors.npy` [891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 891 or target_col == 891). Every well: [[GRIPAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIPAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
