---
symbol: "JAM2"
type: "gene"
col: 7830
ensembl_id: "ENSG00000154721"
name: "junctional adhesion molecule 2"
location: "21q21.3"
module: 80
arm: "+"
pooled_cpm: 6.07
n_lines_expressing: 22
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 20
direction_downstream: 23
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# JAM2

*junctional adhesion molecule 2* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.24× (z +17.8, q 0e+00, up in 11 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.480× (z -7.8, q 2e-12, down in 14 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLAGL1]] (+0.66, fdr 1e-05), [[LINC02968]] (+0.64, fdr 7e-06), [[IRAG2]] (+0.63, fdr 1e-05); moves opposite to [[BCR]] (-0.60, fdr 3e-05), [[HERC2P9]] (-0.59, fdr 7e-05), [[PIK3CB]] (-0.58, fdr 9e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 23 go from it, the strongest it → [[IPO9-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.24×** | +17.8 | 0e+00 | 11/19 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +11.8 | 8e-30 | 8/18 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +10.6 | 4e-24 | 1/13 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +10.2 | 5e-22 | 2/9 (A498, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.45×** | +9.6 | 1e-19 | 7/18 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +9.1 | 5e-18 | 1/10 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +7.7 | 1e-12 | 5/20 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.5 | 2e-06 | 6/15 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.1 | 3e-05 | 4/17 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +4.9 | 4e-05 | 8/19 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +4.7 | 1e-04 | 7/19 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.3 | 7e-04 | 2/19 (MIA PaCa-2, HS-578T) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.6 | 0.012 | 0/9 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.3 | 0.042 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.049 | 2/19 (LOX-IMVI, HOP62) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.087 | 0/17 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7830.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.480×** | -7.8 | 2e-12 | 14/19 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.620×** | -5.1 | 9e-05 | 14/16 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.661×** | -4.4 | 0.002 | 12/20 (A-172, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.669×** | -4.3 | 0.002 | 13/19 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.677×** | -4.2 | 0.003 | 6/18 (A498, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.696×** | -3.9 | 0.009 | 9/18 (LOX-IMVI, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.733×** | -3.3 | 0.069 | 5/18 (A498, HS-578T, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 78.7 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -19.7) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.139× (z -17.3) |
| [[hTERT-HPNE (line)]] | wt | 37.2 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -11.1) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.147× (z -9.5) |
| [[SNU-423 (line)]] | alt | 27.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0409× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0792× (z -15.5) |
| [[A498 (line)]] | wt | 3.26 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 30.8× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 11.1× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 41.2 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0985× (z -14.7) |
| [[H4 (line)]] | wt | 32.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 5.95 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0374× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 7.81 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0836× (z -9.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 3.16 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 40.3× (z +10.7) | — |
| [[A-427 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.721 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.726 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.897 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.642 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAGL1]] | +0.66 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[LINC02968]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[IRAG2]] | +0.63 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ZEB2]] | +0.63 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[MAGI2]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SSPN]] | +0.61 | +0.46 / +0.45 | both halves | 3e-05 | pathway: Extracellular matrix organization |
| [[LINC02335]] | +0.61 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[ATP23]] | +0.60 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[IPO9-AS1]] | +0.59 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[LINC02100]] | +0.59 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[RBMS3]] | +0.59 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[CCL5]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCR]] | -0.60 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[HERC2P9]] | -0.59 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[PIK3CB]] | -0.58 | -0.57 / -0.36 | both halves | 9e-05 | pathway: Cell surface interactions at the vascular wall |
| [[HERC2P3]] | -0.58 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[HERC2]] | -0.57 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[HERC2P2]] | -0.57 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[LYPLA1]] | -0.56 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[NAPG]] | -0.54 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[FBXW2]] | -0.50 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[UBAC2]] | -0.50 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[TEX2]] | -0.50 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[APPL2]] | -0.49 | -0.38 / -0.42 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 3, C 17. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers JAM2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises JAM2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02100]] | B | LINC02100 activity raises JAM2's level | lines that do not express LINC02100 (9) vs lines expressing it (41) | 2.07× lower at baseline in the lines without LINC02100 | 0.0999 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, RASA3 |
| [[MME]] | C | MME activity raises JAM2's level | lines that do not express MME (30) vs lines expressing it (20) | 4.04× lower at baseline in the lines without MME | 0.007 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[ZEB2]] | C | ZEB2 activity raises JAM2's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 3.70× lower at baseline in the lines without ZEB2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[MIR137HG]] | C | MIR137HG activity raises JAM2's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 2.59× lower at baseline in the lines without MIR137HG | 0.030 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |
| [[TWIST1]] | C | TWIST1 activity raises JAM2's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 2.85× lower at baseline in the lines without TWIST1 | 0.035 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[LINC01435]] | C | LINC01435 activity raises JAM2's level | lines that do not express LINC01435 (37) vs lines expressing it (13) | 3.26× lower at baseline in the lines without LINC01435 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000203434, TMPRSS15, ENSG00000224865; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises JAM2's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 3.71× lower at baseline in the lines without ABI3BP | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[MSC]] | C | MSC activity raises JAM2's level | lines that do not express MSC (34) vs lines expressing it (16) | 3.84× lower at baseline in the lines without MSC | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[MAGI2-AS3]] | C | MAGI2-AS3 activity raises JAM2's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 3.97× lower at baseline in the lines without MAGI2-AS3 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[LINC00504]] | C | LINC00504 activity raises JAM2's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 2.31× lower at baseline in the lines without LINC00504 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 14, C 9. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IPO9-AS1]] | B | JAM2 activity raises IPO9-AS1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without JAM2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[MSANTD3-TMEFF1]] | B | JAM2 activity raises MSANTD3-TMEFF1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without JAM2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[LINC02100]] | B | JAM2 activity raises LINC02100's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 2.55× lower at baseline in the lines without JAM2 | 0.019 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[NR2F2-AS1]] | B | JAM2 activity raises NR2F2-AS1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without JAM2 | 0.022 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[ICAM5]] | B | JAM2 activity raises ICAM5's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without JAM2 | 0.038 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[ZBTB1]] | B | JAM2 activity raises ZBTB1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.35× lower at baseline in the lines without JAM2 | 0.041 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[LYPLA1]] | B | JAM2 activity lowers LYPLA1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.34× higher at baseline in the lines without JAM2 | 0.055 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[TRPC1]] | B | JAM2 activity raises TRPC1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 2.59× lower at baseline in the lines without JAM2 | 0.056 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[TENT5A]] | B | JAM2 activity raises TENT5A's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 2.83× lower at baseline in the lines without JAM2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[C1S]] | B | JAM2 activity raises C1S's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.65× lower at baseline in the lines without JAM2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[LINC01500]] | B | JAM2 activity raises LINC01500's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.79× lower at baseline in the lines without JAM2 | 0.078 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[PLA2G4C]] | B | JAM2 activity raises PLA2G4C's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without JAM2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.2, 22.5); signed map (41.3, 22.9). **Vector** length 55.2, 14.1% of its response variance represented; |z| ≥ 3 in 482 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +17.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +0.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.8 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | -7.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -1.4 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | junctional adhesion molecule 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:25,639,258-25,717,562 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VE-JAM, JAM-B, JAMB, CD322, JAM-2; previously C21orf43 |
| Gene groups (HGNC) | CD molecules; V-set domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Reactome | 4 pathways, smallest: Integrin cell surface interactions; Cell surface interactions at the vascular wall; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P57087](https://www.uniprot.org/uniprotkb/P57087) (Junctional adhesion molecule B):

> Junctional adhesion protein that mediates heterotypic cell-cell interactions with its cognate receptor JAM3 to regulate different cellular processes. Plays a role in homing and mobilization of hematopoietic stem and progenitor cells within the bone marrow. At the surface of bone marrow stromal cells, it contributes to the retention of the hematopoietic stem and progenitor cells expressing JAM3. Plays a central role in leukocytes extravasation by facilitating not only transmigration but also …

**Summary**, from NCBI Gene [58494](https://www.ncbi.nlm.nih.gov/gene/58494):

> This gene belongs to the immunoglobulin superfamily, and the junctional adhesion molecule (JAM) family. The protein encoded by this gene is a type I membrane protein that is localized at the tight junctions of both epithelial and endothelial cells. It acts as an adhesive ligand for interacting with a variety of immune cell types, and may play a role in lymphocyte homing to secondary lymphoid organs. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:14686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14686) · Entrez [58494](https://www.ncbi.nlm.nih.gov/gene/58494) · UniProt [P57087](https://www.uniprot.org/uniprotkb/P57087) · Ensembl [ENSG00000154721](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154721)

## Data

Gene col 7830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7830); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7830]; `tensor/DDL_lfc|DDL_z.npy` [7830]; `embed/gene_vectors.npy` [7830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7830 or target_col == 7830). Every well: [[JAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
