---
symbol: "IFI35"
type: "gene"
col: 880
ensembl_id: "ENSG00000068079"
name: "interferon induced protein 35"
location: "17q21.31"
module: 32
arm: "+"
pooled_cpm: 17.12
n_lines_expressing: 46
n_dd_up: 18
n_dd_down: 31
n_dd_up_clean: 18
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 51
direction_downstream: 37
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFI35

*interferon induced protein 35* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.87× (z +5.8, q 5e-06, up in 28 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.361× (z -13.8, q 1e-40, down in 35 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OAS1]] (+0.93, fdr 7e-06), [[PARP9]] (+0.93, fdr 7e-06), [[XAF1]] (+0.92, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 51 arrows point to it, the strongest [[CD5L]] → it (grade B ⚠); 37 go from it, the strongest it → [[IFIH1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.87×** | +5.8 | 5e-06 | 28/42 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.80×** | +5.6 | 5e-06 | 31/43 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.03×** | +4.8 | 2e-04 | 28/36 (Hs 766T, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.68×** | +4.8 | 2e-04 | 25/42 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +4.8 | 2e-04 | 25/43 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.58×** | +4.4 | 0.001 | 20/42 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.60×** | +4.3 | 0.001 | 25/44 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 0.001 | 22/43 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.40×** | +4.2 | 0.002 | 20/44 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.78×** | +3.9 | 0.005 | 13/41 (LoVo, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.52×** | +3.8 | 0.009 | 15/41 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.010 | 22/44 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.70×** | +3.6 | 0.012 | 18/41 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.027 | 20/43 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.077 | 15/44 (AsPC-1, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 880.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.361×** | -13.8 | 1e-40 | 35/42 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.261×** | -12.9 | 2e-35 | 40/43 (RPMI-7951, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.267×** | -12.7 | 2e-34 | 39/43 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.303×** | -11.4 | 4e-28 | 35/43 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.465×** | -10.4 | 4e-23 | 30/41 (A549, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.511×** | -9.1 | 8e-18 | 33/44 (A549, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.399×** | -8.8 | 1e-16 | 29/42 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.404×** | -8.7 | 3e-16 | 31/41 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.491×** | -6.8 | 6e-10 | 25/43 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.464×** | -6.6 | 2e-09 | 30/43 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.512×** | -6.4 | 7e-09 | 24/40 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.527×** | -6.1 | 4e-08 | 27/42 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.663×** | -5.6 | 1e-06 | 23/44 (COLO 205, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -5.5 | 1e-06 | 26/39 (A549, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.559×** | -5.2 | 6e-06 | 22/41 (SNU-423, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 31.5 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0938× (z -17.4) |
| [[A-172 (line)]] | wt | 50.2 | 0 | 10 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.178× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 30.8 | 0 | 10 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.183× (z -15.2) |
| [[LoVo (line)]] | wt | 29.1 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 29.6 | 0 | 7 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0403× (z -15.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.0579× (z -14.5) |
| [[SNU-423 (line)]] | alt | 30.3 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -12.4) |
| [[HS-578T (line)]] | alt | 25.4 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 32.2 | 0 | 6 | — | [[Auranofin (drug)]] 5 µM 0.0704× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 45.4 | 0 | 5 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.198× (z -15.4) |
| [[COLO 205 (line)]] | alt | 40.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 17.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -16.6) |
| [[A498 (line)]] | wt | 33.5 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.289× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 22.8 | 0 | 4 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.187× (z -12.4) |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0492× (z -12.2) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.148× (z -11.4) |
| [[J82 (line)]] | alt | 14.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.9× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 3 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0841× (z -10.8) |
| [[RKO (line)]] | wt | 14.7 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.0521× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.199× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 48.7 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.295× (z -11.3) |
| [[A-427 (line)]] | wt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -11.1) |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.05 µM 0.0572× (z -9.1) |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0514× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 4.81 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0660× (z -11.6) |
| [[KATO III (line)]] | alt | 9.52 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.103× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 18.1 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.258× (z -8.8) |
| [[PANC-1 (line)]] | alt | 8.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.7) |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -10.3) |
| [[AN3 CA (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OAS1]] | +0.93 | +0.89 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 916 |
| [[PARP9]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 882 |
| [[XAF1]] | +0.92 | +0.84 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 852 |
| [[IFIT3]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 926 |
| [[SLC15A3]] | +0.91 | +0.81 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[MX1]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 909 |
| [[IFI44]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 924 |
| [[CMPK2]] | +0.91 | +0.84 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 594 |
| [[OAS2]] | +0.91 | +0.84 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 908 |
| [[RSAD2]] | +0.91 | +0.84 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 845 |
| [[SAMD9L]] | +0.90 | +0.83 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 820 |
| [[IFIT1]] | +0.90 | +0.85 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 876 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 26, C 25. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD5L]] | B | CD5L activity raises IFI35's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without CD5L | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises IFI35's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.28× lower at baseline in the lines without TRIM22 | 0.007 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[CMPK2]] | B | CMPK2 activity raises IFI35's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without CMPK2 | 0.010 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[OAS2]] | B | OAS2 activity raises IFI35's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without OAS2 | 0.011 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[MX1]] | B | MX1 activity raises IFI35's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without MX1 | 0.013 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[PARP9]] | B | PARP9 activity raises IFI35's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.64× lower at baseline in the lines without PARP9 | 0.014 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[ODF3B]] | B | ODF3B activity raises IFI35's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without ODF3B | 0.018 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[GBP4]] | B | GBP4 activity raises IFI35's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.13× lower at baseline in the lines without GBP4 | 0.024 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[OAS1]] | B | OAS1 activity raises IFI35's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without OAS1 | 0.027 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises IFI35's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.83× lower at baseline in the lines without SAMD9L | 0.031 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[TYMP]] | B | TYMP activity raises IFI35's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without TYMP | 0.036 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[BTC]] | B | BTC activity raises IFI35's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.20× lower at baseline in the lines without BTC | 0.039 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 0, C 37. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIH1]] | C | IFI35 activity raises IFIH1's level | lines that do not express IFI35 (4) vs lines expressing it (46) | 4.10× lower at baseline in the lines without IFI35 | 0.003 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, ISG15, BIRC3; maybe low, not absent; co-absent with the target |
| [[USP18]] | C | IFI35's natural level strengthens USP18's drug response | IFI35's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.78, reverse +0.69; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | IFI35's natural level strengthens IFIT5's drug response | IFI35's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.80; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | IFI35's natural level strengthens TDRD7's drug response | IFI35's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.65; direction not clear | 0.012 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[OASL]] | C | IFI35's natural level strengthens OASL's drug response | IFI35's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.10; direction not clear | 0.017 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRANK1]] | C | IFI35's natural level strengthens TRANK1's drug response | IFI35's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.53; direction not clear | 0.018 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | IFI35 activity raises PARP12's level | lines that do not express IFI35 (4) vs lines expressing it (46) | 3.86× lower at baseline in the lines without IFI35 | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, ISG15, BIRC3; maybe low, not absent; co-absent with the target |
| [[TRIM5]] | C | IFI35's natural level strengthens TRIM5's drug response | IFI35's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.58; direction not clear | 0.023 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[CMTR1]] | C | IFI35's natural level strengthens CMTR1's drug response | IFI35's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.61; direction not clear | 0.023 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | IFI35's natural level strengthens IFIT1's drug response | IFI35's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.59; direction not clear | 0.025 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | IFI35's natural level strengthens IRF9's drug response | IFI35's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.64; direction not clear | 0.025 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TAP1]] | C | IFI35 activity raises TAP1's level | lines that do not express IFI35 (4) vs lines expressing it (46) | 2.48× lower at baseline in the lines without IFI35 | 0.031 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, ISG15, BIRC3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.956). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.2, 53.7); signed map (64.4, 31.7). **Vector** length 130, 42.2% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.87 to 23); *Interferon gamma signaling* (reactome, mean cos +0.79 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.84 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.3 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.2 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +4.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.7 | -13.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.4 | -9.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.8 | -8.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.8 | -8.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.1 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced protein 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,006,740-43,014,456 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IFP35 |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Interferon alpha/beta signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [P80217](https://www.uniprot.org/uniprotkb/P80217) (Interferon-induced 35 kDa protein):

> Acts as a signaling pathway regulator involved in innate immune system response. In response to interferon IFN-alpha, associates in a complex with signaling pathway regulator NMI to regulate immune response; the complex formation prevents proteasome-mediated degradation of IFI35 and correlates with IFI35 dephosphorylation. In complex with NMI, inhibits virus-triggered type I interferon/IFN-beta production. In complex with NMI, negatively regulates nuclear factor NF-kappa-B signaling by …

**Summary**, from NCBI Gene [3430](https://www.ncbi.nlm.nih.gov/gene/3430):

> Enables identical protein binding activity. Involved in several processes, including macrophage activation involved in immune response; negative regulation of non-canonical NF-kappaB signal transduction; and positive regulation of defense response. Located in several cellular components, including cytosol; nuclear lumen; and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:5399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5399) · Entrez [3430](https://www.ncbi.nlm.nih.gov/gene/3430) · UniProt [P80217](https://www.uniprot.org/uniprotkb/P80217) · Ensembl [ENSG00000068079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068079)

## Data

Gene col 880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 880); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 880]; `tensor/DDL_lfc|DDL_z.npy` [880]; `embed/gene_vectors.npy` [880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 880 or target_col == 880). Every well: [[IFI35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFI35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
