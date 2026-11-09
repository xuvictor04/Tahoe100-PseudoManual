---
symbol: "CACNB2"
type: "gene"
col: 9219
ensembl_id: "ENSG00000165995"
name: "calcium voltage-gated channel auxiliary subunit beta 2"
location: "10p12"
module: 9
arm: "+"
pooled_cpm: 22.54
n_lines_expressing: 19
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 15
direction_downstream: 6
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CACNB2

*calcium voltage-gated channel auxiliary subunit beta 2* — 10p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.16× (z +19.8, q 0e+00, up in 8 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.709× (z -4.2, q 0.017, down in 8 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD8]] (+0.68, fdr 7e-06), [[LINC02197]] (+0.64, fdr 1e-05), [[KHDRBS2]] (+0.62, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[EPHA5-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.16×** | +19.8 | 0e+00 | 8/16 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +12.6 | 9e-34 | 2/12 (NCI-H1573, HCT15) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +9.0 | 4e-17 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +8.3 | 2e-14 | 4/15 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +7.9 | 4e-13 | 2/14 (LS 180, H4) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +7.0 | 3e-10 | 5/17 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +6.9 | 5e-10 | 3/16 (NCI-H23, SW 900, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +6.7 | 1e-09 | 7/14 (H4, LS 180, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +6.5 | 6e-09 | 8/17 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.1 | 2e-05 | 3/17 (A-427, H4, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +4.5 | 4e-04 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.45×** | +4.3 | 1e-03 | 1/14 (NCI-H23) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.003 | 6/16 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.6 | 0.011 | 4/13 (A-427, HCT15, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.027 | 0/15 | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.037 | 7/17 (LS 180, C32, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9219.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -4.2 | 0.017 | 8/16 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.736×** | -3.7 | 0.055 | 4/16 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.741×** | -3.6 | 0.055 | 5/16 (CHP-212, LoVo, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.824× | -3.3 | 0.13 | 7/17 (CHP-212, HCT15, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -3.0 | 0.23 | 0/17 | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.764× | -3.0 | 0.23 | 0/16 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 116 | 2 | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -12.3) |
| [[LS 180 (line)]] | wt | 223 | 1 | 6 (6 ⚠) | [[Binimetinib (drug)]] 5 µM 2.85× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 115 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0818× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -10.8) |
| [[CHP-212 (line)]] | wt | 230 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -13.8) |
| [[A-427 (line)]] | wt | 15.3 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.99× (z +8.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0968× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 6.35 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 87.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 32.4 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~13% of this change |
| [[NCI-H2030 (line)]] | alt | 12.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.98× (z +8.7) | — |
| [[A-172 (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.49 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.56 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.90 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD8]] | +0.68 | +0.65 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[LINC02197]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[KHDRBS2]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[RALYL]] | +0.61 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[PCDH9]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CDH10]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[NKAIN2]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[SYT4]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[LRFN2]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 | pathway: Neuronal System |
| [[KCNMB2]] | +0.58 | +0.47 / +0.54 | both halves | 2e-05 | pathway: Neuronal System |
| [[PDE7B]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SOX2]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 1, C 14. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CACNB2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02055]] | C | LINC02055 activity raises CACNB2's level | lines that do not express LINC02055 (30) vs lines expressing it (20) | 2.53× lower at baseline in the lines without LINC02055 | 0.004 | ⚠ within organs, on part of the lines; also absent: BAGE2, LINC01446, ENSG00000234352; maybe low, not absent; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises CACNB2's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 4.15× lower at baseline in the lines without GPRIN3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[KCNK2]] | C | KCNK2 activity raises CACNB2's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without KCNK2 | 0.013 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; co-absent with the target |
| [[GUCY1A1]] | C | GUCY1A1 activity raises CACNB2's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without GUCY1A1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises CACNB2's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.11× lower at baseline in the lines without KCNE4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises CACNB2's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 4.87× lower at baseline in the lines without MUC6 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises CACNB2's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 2.41× lower at baseline in the lines without EPHA5 | 0.030 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[NAA11]] | C | NAA11 activity raises CACNB2's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.00× lower at baseline in the lines without NAA11 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[SFTA3-1]] | C | SFTA3-1 activity raises CACNB2's level | lines that do not express SFTA3-1 (35) vs lines expressing it (15) | 2.44× lower at baseline in the lines without SFTA3-1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01035, ZNF736P9Y, ENSG00000289418; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises CACNB2's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 3.01× lower at baseline in the lines without GREM2 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[NKAIN2]] | C | NKAIN2 activity raises CACNB2's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 2.86× lower at baseline in the lines without NKAIN2 | 0.089 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA5-AS1]] | C | CACNB2 activity raises EPHA5-AS1's level | lines that do not express CACNB2 (31) vs lines expressing it (19) | 2.61× lower at baseline in the lines without CACNB2 | 0.036 | ⚠ within organs, on part of the lines; also absent: SFTA3-1, DPP10, LINC01035; maybe low, not absent; co-absent with the target |
| [[EPHA5]] | C | CACNB2 activity raises EPHA5's level | lines that do not express CACNB2 (31) vs lines expressing it (19) | 4.33× lower at baseline in the lines without CACNB2 | 0.037 | ⚠ within organs, on part of the lines; also absent: SFTA3-1, DPP10, LINC01035; maybe low, not absent; co-absent with the target |
| [[LINC02055]] | C | CACNB2 activity raises LINC02055's level | lines that do not express CACNB2 (31) vs lines expressing it (19) | 2.58× lower at baseline in the lines without CACNB2 | 0.056 | ⚠ within organs, on part of the lines; also absent: SFTA3-1, DPP10, LINC01035; maybe low, not absent; co-absent with the target |
| [[CRISPLD1]] | C | CACNB2 activity raises CRISPLD1's level | lines that do not express CACNB2 (31) vs lines expressing it (19) | 3.79× lower at baseline in the lines without CACNB2 | 0.062 | ⚠ within organs, on part of the lines; also absent: SFTA3-1, DPP10, LINC01035; maybe low, not absent; co-absent with the target |
| [[VIPR2]] | C | CACNB2 activity raises VIPR2's level | lines that do not express CACNB2 (31) vs lines expressing it (19) | 1.63× lower at baseline in the lines without CACNB2 | 0.063 | ⚠ within organs, on part of the lines; also absent: SFTA3-1, DPP10, LINC01035; maybe low, not absent; co-absent with the target |
| [[FGF13]] | C | CACNB2 activity raises FGF13's level | lines that do not express CACNB2 (31) vs lines expressing it (19) | 2.62× lower at baseline in the lines without CACNB2 | 0.070 | ⚠ within organs, on part of the lines; also absent: SFTA3-1, DPP10, LINC01035; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.3, 37.3); signed map (42.9, 34.4). **Vector** length 56.2, 16.0% of its response variance represented; |z| ≥ 3 in 518 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +19.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +1.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.1 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12 — chr10:18,140,424-18,543,557 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MYSB, CACNLB2 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; Calcium voltage-gated channel auxiliary beta subunits; SH3 domain containing |
| Reactome | 20 pathways, smallest: Phase 2 - plateau phase; Presynaptic depolarization and calcium channel opening; Mechanical load activates signaling by PIEZO1 and integrins in osteocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08289](https://www.uniprot.org/uniprotkb/Q08289) (Voltage-dependent L-type calcium channel subunit beta-2):

> Beta subunit of voltage-dependent calcium channels which contributes to the function of the calcium channel by increasing peak calcium current (By similarity). Plays a role in shifting voltage dependencies of activation and inactivation of the channel (By similarity). May modulate G protein inhibition (By similarity). May contribute to beta-adrenergic augmentation of Ca(2+) influx in cardiomyocytes, thereby regulating increases in heart rate and contractile force. Involved in membrane targeting …

**Summary**, from NCBI Gene [783](https://www.ncbi.nlm.nih.gov/gene/783):

> This gene encodes a subunit of a voltage-dependent calcium channel protein that is a member of the voltage-gated calcium channel superfamily. The gene product was originally identified as an antigen target in Lambert-Eaton myasthenic syndrome, an autoimmune disorder. Mutations in this gene are associated with Brugada syndrome. Alternatively spliced variants encoding different isoforms have been described. [provided by RefSeq, Feb 2013]

**Accessions** — [HGNC:1402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1402) · Entrez [783](https://www.ncbi.nlm.nih.gov/gene/783) · UniProt [Q08289](https://www.uniprot.org/uniprotkb/Q08289) · Ensembl [ENSG00000165995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165995)

## Data

Gene col 9219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9219); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9219]; `tensor/DDL_lfc|DDL_z.npy` [9219]; `embed/gene_vectors.npy` [9219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9219 or target_col == 9219). Every well: [[CACNB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
