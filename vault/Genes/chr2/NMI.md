---
symbol: "NMI"
type: "gene"
col: 4449
ensembl_id: "ENSG00000123609"
name: "N-myc and STAT interactor"
location: "2q23.3"
module: 32
arm: "+"
pooled_cpm: 24.93
n_lines_expressing: 46
n_dd_up: 24
n_dd_down: 31
n_dd_up_clean: 22
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 65
direction_downstream: 17
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# NMI

*N-myc and STAT interactor* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.53× (z +11.0, q 2e-25, up in 36 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.138× (z -23.4, q 0e+00, down in 44 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARP14]] (+0.91, fdr 7e-06), [[PHF11]] (+0.89, fdr 7e-06), [[DTX3L]] (+0.88, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 65 arrows point to it, the strongest [[ALPK1]] → it (grade B ⚠); 17 go from it, the strongest it → [[OASL]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.53×** | +11.0 | 2e-25 | 36/44 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.81×** | +7.0 | 5e-10 | 30/44 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +5.9 | 8e-07 | 30/43 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 9e-05 | 25/44 (Hs 766T, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 9e-05 | 25/44 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.51×** | +4.7 | 3e-04 | 26/43 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.44×** | +4.4 | 1e-03 | 20/44 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 0.001 | 21/44 (LoVo, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +4.3 | 0.001 | 24/43 (NCI-H2347, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.003 | 21/44 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.003 | 20/43 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.012 | 15/44 (AsPC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.012 | 14/44 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.022 | 18/42 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.024 | 13/42 (Panc 03.27, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4449.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.138×** | -23.4 | 0e+00 | 44/44 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.153×** | -22.2 | 0e+00 | 44/44 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.169×** | -21.0 | 0e+00 | 43/44 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.333×** | -13.0 | 2e-36 | 42/44 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.364×** | -11.9 | 9e-31 | 40/43 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.558×** | -9.7 | 3e-20 | 31/44 (NCI-H1573, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.592×** | -8.7 | 2e-16 | 29/44 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.303×** | -7.4 | 1e-11 | 34/44 (A-172, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.644×** | -7.3 | 2e-11 | 31/44 (RKO, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.548×** | -7.1 | 8e-11 | 31/42 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.555×** | -6.9 | 2e-10 | 30/44 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.559×** | -6.9 | 3e-10 | 34/44 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.560×** | -6.8 | 3e-10 | 30/44 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.563×** | -6.8 | 5e-10 | 32/44 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.694×** | -6.1 | 5e-08 | 28/44 (A549, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.599×** | -6.0 | 6e-08 | 31/43 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 47.4 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0485× (z -22.5) |
| [[RPMI-7951 (line)]] | alt | 41.6 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.5) |
| [[A498 (line)]] | wt | 63.4 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -17.4) |
| [[A549 (line)]] | wt | 36.2 | 0 | 7 | — | [[Belinostat (drug)]] 5 µM 0.0526× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 45.7 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0555× (z -17.0) |
| [[NCI-H2347 (line)]] | alt | 42.5 | 1 | 6 | [[Harringtonine (drug)]] 0.5 µM 3.51× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -18.5) |
| [[AsPC-1 (line)]] | alt | 30.6 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0926× (z -13.7) |
| [[SNU-423 (line)]] | alt | 32.7 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.0743× (z -16.1) |
| [[COLO 205 (line)]] | alt | 52.8 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0385× (z -21.1) |
| [[J82 (line)]] | alt | 24.7 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -9.7) |
| [[LoVo (line)]] | wt | 27.9 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0770× (z -17.9) |
| [[NCI-H1573 (line)]] | alt | 19.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0774× (z -15.8) |
| [[PANC-1 (line)]] | alt | 29.9 | 1 | 4 | [[Harringtonine (drug)]] 0.5 µM 3.21× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -18.6) |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.126× (z -12.5) |
| [[BT-474 (line)]] | alt | 25.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0715× (z -14.2) |
| [[KATO III (line)]] | alt | 26.5 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0507× (z -18.1) |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0781× (z -16.9) |
| [[NCI-H23 (line)]] | alt | 21.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0613× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -13.5) |
| [[RKO (line)]] | wt | 27.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0754× (z -13.9) |
| [[SW480 (line)]] | alt | 8.45 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0824× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.124× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 38.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -15.6) |
| [[Hs 766T (line)]] | wt | 29.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -13.0) |
| [[HT-29 (line)]] | alt | 24.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.120× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 27.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 39.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -12.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.116× (z -12.3) |
| [[H4 (line)]] | wt | 16.3 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0946× (z -9.6) |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -11.6) |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0968× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -11.4) |
| [[SW 900 (line)]] | alt | 17.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -9.4) |
| [[A-427 (line)]] | wt | 16.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.180× (z -9.2) |
| [[C32 (line)]] | wt | 14.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -8.8) |
| [[AN3 CA (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP14]] | +0.91 | +0.87 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PHF11]] | +0.89 | +0.85 / +0.89 | both halves | 7e-06 | STRING 570 |
| [[DTX3L]] | +0.88 | +0.82 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[IFIT5]] | +0.87 | +0.81 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[SAMD9L]] | +0.86 | +0.78 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PSMB8]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 566 |
| [[TRANK1]] | +0.86 | +0.80 / +0.87 | both halves | 7e-06 |  |
| [[DDX60]] | +0.85 | +0.78 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFIT3]] | +0.85 | +0.76 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 423 |
| [[IFIH1]] | +0.84 | +0.75 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 637 |
| [[PARP9]] | +0.84 | +0.74 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 593 |
| [[EIF2AK2]] | +0.84 | +0.77 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*65 arrows, 65 of them with an alert ⚠; grade A 0, B 39, C 26. Shown: the 12 strongest; 53 more arrows (53 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALPK1]] | B | ALPK1 activity raises NMI's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 2.93× lower at baseline in the lines without ALPK1 | 0.005 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises NMI's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without OAS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity strengthens NMI's drug response | lines that do not express RSAD2 (12) vs lines expressing it (32) | the lines without RSAD2 respond 0.67× as strongly (z diff +2.20); strongest at Homoharringtonine 5 µM: 0.76x vs 0.54x (z diff +3.4) | 0.012 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS; target measured in part of the lines; artifact flags |
| [[GBP4]] | B | GBP4 activity raises NMI's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.36× lower at baseline in the lines without GBP4 | 0.013 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[PARP9]] | B | PARP9 activity strengthens NMI's drug response | lines that do not express PARP9 (5) vs lines expressing it (39) | the lines without PARP9 respond 0.73× as strongly (z diff +2.26); strongest at Panobinostat 0.05 µM: 0.50x vs 0.30x (z diff +3.7) | 0.014 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TRIM34]] | B | TRIM34 activity raises NMI's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 3.09× lower at baseline in the lines without TRIM34 | 0.015 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[ETV7]] | B | ETV7 activity strengthens NMI's drug response | lines that do not express ETV7 (12) vs lines expressing it (32) | the lines without ETV7 respond 0.74× as strongly (z diff +1.55); strongest at Panobinostat 0.5 µM: 0.23x vs 0.13x (z diff +2.4) | 0.016 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MX1]] | B | MX1 activity raises NMI's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.92× lower at baseline in the lines without MX1 | 0.016 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[BATF2]] | B | BATF2 activity raises NMI's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without BATF2 | 0.020 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[ODF3B]] | B | ODF3B activity raises NMI's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without ODF3B | 0.023 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[IL15RA]] | B | IL15RA activity raises NMI's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 2.42× lower at baseline in the lines without IL15RA | 0.025 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[CGAS]] | B | CGAS activity raises NMI's level | lines that do not express CGAS (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without CGAS | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OASL]] | C | NMI's natural level strengthens OASL's drug response | NMI's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.37; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP10]] | C | NMI's natural level strengthens PARP10's drug response | NMI's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.68; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRANK1]] | C | NMI's natural level strengthens TRANK1's drug response | NMI's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.69; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TMEM62]] | C | NMI's natural level strengthens TMEM62's drug response | NMI's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.60; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB8]] | C | NMI's natural level strengthens PSMB8's drug response | NMI's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.60; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SLFN5]] | C | NMI activity raises SLFN5's level | lines that do not express NMI (4) vs lines expressing it (46) | 3.82× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91; its own permutation p |
| [[C1RL]] | C | NMI activity raises C1RL's level | lines that do not express NMI (4) vs lines expressing it (46) | 3.18× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91; its own permutation p |
| [[ALPK1]] | C | NMI activity raises ALPK1's level | lines that do not express NMI (4) vs lines expressing it (46) | 2.92× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91; its own permutation p |
| [[IL15]] | C | NMI activity raises IL15's level | lines that do not express NMI (4) vs lines expressing it (46) | 2.29× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91; its own permutation p |
| [[TRIM5]] | C | NMI activity raises TRIM5's level | lines that do not express NMI (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91; its own permutation p |
| [[RBM43]] | C | NMI activity raises RBM43's level | lines that do not express NMI (4) vs lines expressing it (46) | 1.76× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91; its own permutation p |
| [[BTN3A1]] | C | NMI activity raises BTN3A1's level | lines that do not express NMI (4) vs lines expressing it (46) | 1.71× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.866). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.1, 53.4); signed map (62.3, 31.6). **Vector** length 132, 44.4% of its response variance represented; |z| ≥ 3 in 1,324 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.76 to 23); *Interferon Signaling* (reactome, mean cos +0.72 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.74 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +11.3 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.3 | +7.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.0 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.5 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.5 | +4.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.5 | +5.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.7 | -11.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -6.9 | -8.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.5 | -6.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.2 | -6.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.6 | -5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.9 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | N-myc and STAT interactor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:151,270,470-151,289,894 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INFLAMMATORY_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 5 pathways, smallest: SARS-CoV-1 activates/modulates innate immune responses; SARS-CoV-1-host interactions; SARS-CoV-1 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13287](https://www.uniprot.org/uniprotkb/Q13287) (N-myc-interactor):

> Acts as a signaling pathway regulator involved in innate immune system response. In response to interleukin 2/IL2 and interferon IFN-gamma/IFNG, interacts with signal transducer and activator of transcription/STAT which activate the transcription of downstream genes involved in a multitude of signals for development and homeostasis. Enhances the recruitment of CBP/p300 coactivators to STAT1 and STAT5, resulting in increased STAT1- and STAT5-dependent transcription. In response to interferon …

**Summary**, from NCBI Gene [9111](https://www.ncbi.nlm.nih.gov/gene/9111):

> NMYC interactor (NMI) encodes a protein that interacts with NMYC and CMYC (two members of the oncogene Myc family), and other transcription factors containing a Zip, HLH, or HLH-Zip motif. The NMI protein also interacts with all STATs except STAT2 and augments STAT-mediated transcription in response to cytokines IL2 and IFN-gamma. The NMI mRNA has low expression levels in all human fetal and adult tissues tested except brain and has high expression in cancer cell line-myeloid leukemias. …

**Accessions** — [HGNC:7854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7854) · Entrez [9111](https://www.ncbi.nlm.nih.gov/gene/9111) · UniProt [Q13287](https://www.uniprot.org/uniprotkb/Q13287) · Ensembl [ENSG00000123609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123609)

## Data

Gene col 4449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4449); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4449]; `tensor/DDL_lfc|DDL_z.npy` [4449]; `embed/gene_vectors.npy` [4449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4449 or target_col == 4449). Every well: [[NMI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
