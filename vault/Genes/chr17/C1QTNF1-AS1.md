---
symbol: "C1QTNF1-AS1"
type: "gene"
col: 15450
ensembl_id: "ENSG00000265096"
name: "C1QTNF1 antisense RNA 1"
location: "17q25.3"
module: 14
arm: "+"
pooled_cpm: 2.95
n_lines_expressing: 26
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# C1QTNF1-AS1

*C1QTNF1 antisense RNA 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.70× (z +16.1, q 0e+00, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.73× (z +10.5, q 2e-23, up in 8 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.440× (z -6.1, q 7e-07, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1QTNF1]] (+0.76, fdr 7e-06, ⚠ same locus), [[TMEM52B]] (+0.75, fdr 1e-05), [[WAKMAR2]] (+0.69, fdr 9e-06), [[OLR1]] (+0.68, fdr 1e-05); moves opposite to [[PCMT1]] (-0.53, fdr 5e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[CCDC170]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.70×** | +16.1 | 0e+00 | 2/5 (SW480, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.01×** | +13.2 | 1e-37 | 7/9 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.76×** | +10.7 | 3e-24 | 3/5 (SW1417, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.73×** | +10.5 | 2e-23 | 8/17 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +10.1 | 1e-21 | 13/16 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.18×** | +8.1 | 4e-14 | 11/22 (SW480, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.7 | 8e-07 | 10/23 (A498, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +5.5 | 3e-06 | 4/8 (SNU-423, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.89×** | +4.7 | 2e-04 | 12/20 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +4.5 | 4e-04 | 9/17 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.33×** | +4.5 | 4e-04 | 1/7 (NCI-H1792) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +4.4 | 6e-04 | 4/23 (LS 180, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +4.3 | 9e-04 | 7/10 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +4.2 | 0.001 | 6/17 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +4.1 | 0.002 | 8/20 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +4.0 | 0.002 | 0/18 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.04×** | +3.8 | 0.006 | 1/10 (J82) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.54×** | +3.2 | 0.039 | 4/18 (A498, A-172, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.052 | 3/19 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.57×** | +3.1 | 0.053 | 1/12 (NCI-H1792) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.440×** | -6.1 | 7e-07 | 14/22 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.521×** | -4.8 | 4e-04 | 11/21 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.612×** | -3.6 | 0.053 | 14/21 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 19.6 | 4 | 4 (2 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.95× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.0752× (z -13.7) |
| [[SW480 (line)]] | alt | 7.13 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0544× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0628× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0468× (z -13.2) |
| [[J82 (line)]] | alt | 10.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.131× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0225× (z -16.8) |
| [[A-172 (line)]] | wt | 2.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 1.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 3.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.80× (z +8.6) | — |
| [[A-427 (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.949 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.879 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.496 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.593 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1QTNF1]] | +0.76 | +0.73 / +0.60 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TMEM52B]] | +0.75 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[WAKMAR2]] | +0.69 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[OLR1]] | +0.68 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[GFRA1]] | +0.67 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | +0.66 | +0.53 / +0.55 | both halves | 1e-05 | same gene group |
| [[OGFRL1]] | +0.65 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[CLDN16]] | +0.65 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[DRAM1]] | +0.65 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[RBMS3-AS3]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 | same gene group |
| [[KMO]] | +0.65 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[LINC02605]] | +0.64 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[EYS]] | +0.64 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | -0.53 | -0.37 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C1QTNF1-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.9% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises C1QTNF1-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[C1QTNF1]] | C | C1QTNF1 activity raises C1QTNF1-AS1's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 1.53× lower at baseline in the lines without C1QTNF1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC170]] | B | C1QTNF1-AS1 activity raises CCDC170's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without C1QTNF1-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent |
| [[RHCG]] | B | C1QTNF1-AS1 activity raises RHCG's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 1.53× lower at baseline in the lines without C1QTNF1-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent |
| [[TNFAIP6]] | B | C1QTNF1-AS1 activity raises TNFAIP6's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without C1QTNF1-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent |
| [[DENND5B-AS1]] | B | C1QTNF1-AS1 activity lowers DENND5B-AS1's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 1.55× higher at baseline in the lines without C1QTNF1-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent |
| [[IL32]] | B | C1QTNF1-AS1 activity strengthens IL32's drug response | lines that do not express C1QTNF1-AS1 (11) vs lines expressing it (19) | the lines without C1QTNF1-AS1 respond 0.82× as strongly (z diff +0.90); strongest at Idarubicin (hydrochloride) 5 µM: 1.73x vs 2.44x (z diff +2.5) | 0.091 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[C1QTNF1]] | C | C1QTNF1-AS1 activity raises C1QTNF1's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 3.60× lower at baseline in the lines without C1QTNF1-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent; co-absent with the target |
| [[LUM]] | C | C1QTNF1-AS1 activity raises LUM's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without C1QTNF1-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent; co-absent with the target |
| [[MSC]] | C | C1QTNF1-AS1 activity raises MSC's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 1.83× lower at baseline in the lines without C1QTNF1-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent; co-absent with the target |
| [[VCAM1]] | C | C1QTNF1-AS1 activity raises VCAM1's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 2.63× lower at baseline in the lines without C1QTNF1-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.7, 24.6); signed map (43.6, 17.7). **Vector** length 50.2, 11.7% of its response variance represented; |z| ≥ 3 in 547 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.7 | -4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.2 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | -6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | C1QTNF1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q25.3 — chr17:79,018,131-79,027,673 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44351) · Entrez [100507410](https://www.ncbi.nlm.nih.gov/gene/100507410) · Ensembl [ENSG00000265096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265096)

## Data

Gene col 15450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15450); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15450]; `tensor/DDL_lfc|DDL_z.npy` [15450]; `embed/gene_vectors.npy` [15450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15450 or target_col == 15450). Every well: [[C1QTNF1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1QTNF1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
