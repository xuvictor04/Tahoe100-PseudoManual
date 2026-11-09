---
symbol: "OR3A2"
type: "gene"
col: 13312
ensembl_id: "ENSG00000221882"
name: "olfactory receptor family 3 subfamily A member 2"
location: "17p13.3"
module: 108
arm: "+"
pooled_cpm: 2.48
n_lines_expressing: 23
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 2
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# OR3A2

*olfactory receptor family 3 subfamily A member 2* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.36× (z +16.7, q 0e+00, up in 4 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pravastatin (sodium) (drug)]] 5 µM: 0.551× (z -4.1, q 0.029, down in 1 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.136×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGBL4]] (+0.63, fdr 1e-05), [[MIR2052HG]] (+0.62, fdr 1e-05), [[LGSN]] (+0.58, fdr 3e-05).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[LINC02268]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.36×** | +16.7 | 0e+00 | 4/6 (HEC-1-A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.90×** | +10.7 | 2e-24 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.00×** | +9.7 | 4e-20 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.55×** | +9.3 | 2e-18 | 5/9 (SHP-77, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.64×** | +7.7 | 1e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +4.9 | 1e-04 | 3/15 (NCI-H1573, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.8 | 1e-04 | 1/3 (NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +4.7 | 2e-04 | 1/7 (SHP-77) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +4.1 | 0.002 | 1/5 (SHP-77) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +4.1 | 0.002 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.004 | 2/14 (SHP-77, NCI-H1573) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.08×** | +3.7 | 0.011 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.70×** | +3.7 | 0.011 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.6 | 0.014 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.5 | 0.015 | 1/9 (SHP-77) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.97×** | +3.4 | 0.024 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.044 | 2/12 (HEC-1-A, RKO) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.060 | 1/8 (HOP62) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.56×** | +3.0 | 0.078 | 0/6 | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13312.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.551×** | -4.1 | 0.029 | 1/13 (LOX-IMVI) | rises with dose | plate-row cell shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.881× | -3.4 | 0.22 | 4/18 (HOP62, NCI-H661, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 5 µM |  | 0.632× | -3.2 | 0.22 | 2/13 (A-427, NCI-H1573) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 32.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -12.7) |
| [[A-172 (line)]] | wt | 0.553 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.749 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.676 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.708 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.654 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.640 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.661 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.669 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.660 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.934 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.631 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.877 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.668 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.638 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.649 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.576 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGBL4]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MIR2052HG]] | +0.62 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[LGSN]] | +0.58 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[GABRG2]] | +0.58 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[SPAG17]] | +0.57 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[MGAT4C]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ZFHX4-AS1]] | +0.56 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[RIMS2]] | +0.55 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[STPG2]] | +0.55 | +0.57 / +0.36 | both halves | 9e-05 |  |
| [[LINC00648]] | +0.54 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[FGF14]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[RFPL1S]] | +0.53 | +0.46 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OR3A2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GABRG2]] | C | GABRG2 activity raises OR3A2's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.36× lower at baseline in the lines without GABRG2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LINC02492]] | C | LINC02492 activity raises OR3A2's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 1.76× lower at baseline in the lines without LINC02492 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises OR3A2's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 2.53× lower at baseline in the lines without KCNH5 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[MGAT4C]] | C | MGAT4C activity raises OR3A2's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 2.26× lower at baseline in the lines without MGAT4C | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[LINC02616]] | C | LINC02616 activity raises OR3A2's level | lines that do not express LINC02616 (37) vs lines expressing it (13) | 1.86× lower at baseline in the lines without LINC02616 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, ENSG00000287474, FCRLA; co-absent with the target |
| [[CTNNA3]] | C | CTNNA3 activity raises OR3A2's level | lines that do not express CTNNA3 (4) vs lines expressing it (46) | 1.19× lower at baseline in the lines without CTNNA3 | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL10, MYO15B; maybe low, not absent |
| [[ERBB4]] | C | ERBB4 activity raises OR3A2's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 2.02× lower at baseline in the lines without ERBB4 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[LINC00470]] | C | LINC00470 activity raises OR3A2's level | lines that do not express LINC00470 (38) vs lines expressing it (12) | 2.21× lower at baseline in the lines without LINC00470 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, ENSG00000287474, FCRLA; co-absent with the target |
| [[ZIC1]] | C | ZIC1 activity raises OR3A2's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 2.09× lower at baseline in the lines without ZIC1 | 0.091 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02268]] | B | OR3A2 activity raises LINC02268's level | lines that do not express OR3A2 (27) vs lines expressing it (23) | 1.76× lower at baseline in the lines without OR3A2 | 0.012 | ⚠ within organs, on part of the lines; also absent: GRIK1, PAPPA2, LINC01266; maybe low, not absent |
| [[NTNG1]] | C | OR3A2 activity raises NTNG1's level | lines that do not express OR3A2 (27) vs lines expressing it (23) | 1.98× lower at baseline in the lines without OR3A2 | 0.043 | ⚠ within organs, on part of the lines; also absent: GRIK1, PAPPA2, LINC01266; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.405). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.6, 39.7); signed map (48.3, 35.3). **Vector** length 18.4, 3.22% of its response variance represented; |z| ≥ 3 in 286 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +16.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.6 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.6 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.6 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.5 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.5 | +1.3 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.5 | -1.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.4 | -2.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.4 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | olfactory receptor family 3 subfamily A member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:3,276,177-3,386,317 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OLFRA04, OR228, OR17-228 |
| Gene groups (HGNC) | Olfactory receptors, family 3 |
| Reactome | 3 pathways, smallest: Expression and translocation of olfactory receptors; Olfactory Signaling Pathway; Sensory Perception |
| Matched by | ensembl_id |

**Function**, from UniProt [P47893](https://www.uniprot.org/uniprotkb/P47893) (Olfactory receptor 3A2):

> Odorant receptor.

**Summary**, from NCBI Gene [4995](https://www.ncbi.nlm.nih.gov/gene/4995):

> Olfactory receptors interact with odorant molecules in the nose, to initiate a neuronal response that triggers the perception of a smell. The olfactory receptor proteins are members of a large family of G-protein-coupled receptors (GPCR) arising from single coding-exon genes. Olfactory receptors share a 7-transmembrane domain structure with many neurotransmitter and hormone receptors and are responsible for the recognition and G protein-mediated transduction of odorant signals. The olfactory …

**Accessions** — [HGNC:8283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8283) · Entrez [4995](https://www.ncbi.nlm.nih.gov/gene/4995) · UniProt [P47893](https://www.uniprot.org/uniprotkb/P47893) · Ensembl [ENSG00000221882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221882)

## Data

Gene col 13312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13312); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13312]; `tensor/DDL_lfc|DDL_z.npy` [13312]; `embed/gene_vectors.npy` [13312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13312 or target_col == 13312). Every well: [[OR3A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OR3A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
