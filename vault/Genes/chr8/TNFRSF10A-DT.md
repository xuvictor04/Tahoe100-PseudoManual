---
symbol: "TNFRSF10A-DT"
type: "gene"
col: 14466
ensembl_id: "ENSG00000246582"
name: "TNFRSF10A divergent transcript"
location: "8p21.3"
module: 24
arm: "+"
pooled_cpm: 2.79
n_lines_expressing: 39
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TNFRSF10A-DT

*TNFRSF10A divergent transcript* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.79× (z +7.9, q 1e-12, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.41× (z +3.9, q 0.010, up in 6 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.606× (z -4.0, q 0.038, down in 11 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (A-427 0.0796×); [[Cobimetinib (drug)]] 5 µM in 1 line (CFPAC-1 0.0517×); [[Daidzin (drug)]] 0.5 µM in 1 line (CHP-212 0.246×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSUN5P2-1]] (+0.60, fdr 3e-05, ⚠ NSUN5P2-1 in the vector space only through flagged drug-doses), [[NSUN5P1-1]] (+0.60, fdr 2e-05), [[SMIM29]] (+0.56, fdr 1e-05), [[FAM98C]] (+0.54, fdr 3e-05); moves opposite to [[TARDBP]] (-0.57, fdr 1e-05), [[C2CD3]] (-0.54, fdr 1e-04), [[IL18BP]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC01518]] → it (grade B ⚠); 4 go from it, the strongest it → [[LINC01518]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14466.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.79×** | +7.9 | 1e-12 | 4/5 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.42×** | +7.1 | 4e-10 | 8/11 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.94×** | +5.3 | 2e-05 | 6/12 (NCI-H2347, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.1 | 0.007 | 6/14 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.010 | 6/33 (A498, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.38×** | +3.7 | 0.023 | 7/28 (NCI-H2347, HCT15, …) | rises with dose | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.2 | 0.095 | 3/22 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | 1.48× | +3.2 | 0.11 | 8/23 (NCI-H1573, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | 1.51× | +3.1 | 0.12 | 3/7 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.46× | +3.1 | 0.12 | 2/26 (HT-29, SW480) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.88× | +3.0 | 0.12 | 2/23 (LS 180, PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14466.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (A-427 0.0796×); [[Cobimetinib (drug)]] 5 µM in 1 line (CFPAC-1 0.0517×); [[Daidzin (drug)]] 0.5 µM in 1 line (CHP-212 0.246×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.606×** | -4.0 | 0.038 | 11/33 (HCT15, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.36 | 0 | 2 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0796× (z -10.1) |
| [[A549 (line)]] | wt | 3.93 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0680× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 3.31 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0517× (z -9.7) |
| [[CHP-212 (line)]] | wt | 0.915 | 0 | 1 | — | [[Daidzin (drug)]] 0.5 µM 0.246× (z -9.1) |
| [[A-172 (line)]] | wt | 0.205 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.451 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.707 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.761 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.816 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 14 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN5P2-1]] ⚠ | +0.60 | +0.45 / +0.62 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5P1-1]] | +0.60 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[SMIM29]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MTLN]] ⚠ | +0.56 | +0.47 / +0.58 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FAM98C]] | +0.54 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[EML2]] | +0.53 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[POLR1H]] | +0.53 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[ZNF330]] | +0.53 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[MINCR]] | +0.52 | +0.28 / +0.60 | both halves | 3e-04 |  |
| [[F12]] | +0.52 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[CHCHD5]] | +0.51 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[FBXL6]] | +0.51 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[NUDT8]] | +0.51 | +0.31 / +0.63 | both halves | 2e-04 |  |
| [[RP9]] | +0.50 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARDBP]] | -0.57 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[C2CD3]] | -0.54 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[IL18BP]] | -0.50 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[HNRNPUL1]] | -0.49 | -0.23 / -0.57 | both halves | 5e-04 |  |
| [[MOB1A]] | -0.47 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[XRCC6]] | -0.47 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[HCFC1]] | -0.46 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[UGGT1]] | -0.46 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[FSTL1]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ZNF407]] | -0.45 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[PRKCSH]] | -0.44 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[ATP2A2]] | -0.44 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01518]] | B | LINC01518 activity lowers TNFRSF10A-DT's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 1.99× higher at baseline in the lines without LINC01518 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2 |
| [[IKZF3]] | B | IKZF3 activity raises TNFRSF10A-DT's level | lines that do not express IKZF3 (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without IKZF3 | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[UPP1]] | B | UPP1 activity raises TNFRSF10A-DT's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without UPP1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01518]] | B | TNFRSF10A-DT activity lowers LINC01518's level | lines that do not express TNFRSF10A-DT (11) vs lines expressing it (39) | 9.44× higher at baseline in the lines without TNFRSF10A-DT | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, SLC16A5, ARHGEF16 |
| [[CHCHD10]] | B | TNFRSF10A-DT activity raises CHCHD10's level | lines that do not express TNFRSF10A-DT (11) vs lines expressing it (39) | 1.96× lower at baseline in the lines without TNFRSF10A-DT | 0.035 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, SLC16A5, ARHGEF16 |
| [[MOB1A]] | B | TNFRSF10A-DT activity raises MOB1A's level | lines that do not express TNFRSF10A-DT (11) vs lines expressing it (39) | 1.24× lower at baseline in the lines without TNFRSF10A-DT | 0.046 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, SLC16A5, ARHGEF16 |
| [[UPP1]] | B | TNFRSF10A-DT activity raises UPP1's level | lines that do not express TNFRSF10A-DT (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without TNFRSF10A-DT | 0.076 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, SLC16A5, ARHGEF16 |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.467). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.7, -21.6); signed map (-28.8, 5.0). **Vector** length 34.4, 4.45% of its response variance represented; |z| ≥ 3 in 544 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +1.6 | +3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.4 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.9 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | TNFRSF10A divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8p21.3 — chr8:23,224,471-23,230,926 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LOC389641, PLACT1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52647) · Entrez [389641](https://www.ncbi.nlm.nih.gov/gene/389641) · Ensembl [ENSG00000246582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246582)

## Data

Gene col 14466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14466); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14466]; `tensor/DDL_lfc|DDL_z.npy` [14466]; `embed/gene_vectors.npy` [14466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14466 or target_col == 14466). Every well: [[TNFRSF10A-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF10A-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
