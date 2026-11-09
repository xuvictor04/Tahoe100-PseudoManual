---
symbol: "ST7L"
type: "gene"
col: 142
ensembl_id: "ENSG00000007341"
name: "suppression of tumorigenicity 7 like"
location: "1p13.2"
module: 88
arm: "+"
pooled_cpm: 33.54
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# ST7L

*suppression of tumorigenicity 7 like* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +11.6, q 2e-28, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.477× (z -9.6, q 7e-19, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WARS2-AS1]] (+0.85, fdr 7e-06), [[RAB30-DT]] (+0.84, fdr 7e-06), [[RFX3-DT]] (+0.81, fdr 1e-05); moves opposite to [[MOSPD3]] (-0.83, fdr 7e-06), [[GMCL1]] (-0.80, fdr 7e-06), [[IGSF8]] (-0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC17A7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 142.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +11.6 | 2e-28 | 43/47 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +10.7 | 3e-24 | 41/47 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +6.0 | 4e-07 | 34/48 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.0 | 7e-05 | 31/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 6e-04 | 29/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.7 | 0.019 | 0/48 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.019 | 22/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.031 | 17/48 (SW480, NCI-H2347, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.036 | 18/48 (NCI-H23, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.039 | 19/48 (NCI-H1792, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.054 | 19/48 (C32, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.477×** | -9.6 | 7e-19 | 41/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.520×** | -8.4 | 9e-15 | 39/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.540×** | -7.9 | 4e-13 | 36/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.645×** | -5.7 | 2e-06 | 29/48 (AN3 CA, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.443×** | -5.5 | 4e-06 | 30/47 (SNU-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.453×** | -5.4 | 8e-06 | 36/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -4.1 | 0.004 | 24/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.770×** | -3.4 | 0.053 | 21/48 (AN3 CA, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.774×** | -3.3 | 0.058 | 19/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.783×** | -3.2 | 0.090 | 18/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.633× | -3.1 | 0.10 | 18/46 (SW48, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.4 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.341× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.322× (z -11.0) |
| [[SW480 (line)]] | alt | 47.9 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 29.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.202× (z -8.7) |
| [[LoVo (line)]] | wt | 35.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.9) | — |
| [[RKO (line)]] | wt | 49.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -11.3) |
| [[A-427 (line)]] | wt | 29.8 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0832× (z -10.0) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 54.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 40.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -9.9) |
| [[SHP-77 (line)]] | alt | 38.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0470× (z -10.9) |
| [[C32 (line)]] | wt | 24.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.196× (z -9.5) |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.131× (z -9.0) |
| [[HCT15 (line)]] | alt | 38.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 34.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 38.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.97× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 30.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.6) | — |
| [[SW48 (line)]] | wt | 30.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +8.5) | — |
| [[A-172 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2-AS1]] | +0.85 | +0.87 / +0.58 | both halves | 7e-06 |  |
| [[RAB30-DT]] | +0.84 | +0.86 / +0.63 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.81 | +0.83 / +0.49 | both halves | 1e-05 |  |
| [[ERCC6L2]] | +0.80 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | +0.77 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[CLHC1]] | +0.77 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[ZC3H4]] | +0.77 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[PPP3CB-AS1]] | +0.76 | +0.74 / +0.42 | both halves | 4e-05 |  |
| [[CYREN]] | +0.76 | +0.82 / +0.57 | both halves | 1e-05 |  |
| [[POGLUT1]] | +0.76 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[RGS5]] | +0.76 | +0.84 / +0.55 | both halves | 1e-05 |  |
| [[LEKR1]] | +0.76 | +0.80 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSPD3]] | -0.83 | -0.80 / -0.73 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.80 | -0.78 / -0.65 | both halves | 7e-06 |  |
| [[IGSF8]] | -0.75 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[MGST3]] | -0.74 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[SDHAP1]] | -0.73 | -0.79 / -0.51 | both halves | 1e-05 |  |
| [[ARL3]] | -0.73 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.73 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[SLC27A1]] | -0.72 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[NTAN1]] | -0.72 | -0.75 / -0.60 | both halves | 7e-06 |  |
| [[YIF1B]] | -0.72 | -0.68 / -0.30 | both halves | 2e-04 |  |
| [[HACE1]] | -0.71 | -0.74 / -0.40 | both halves | 4e-05 |  |
| [[MYPOP]] | -0.71 | -0.66 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC17A7]] | B | SLC17A7 activity raises ST7L's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without SLC17A7 | 0.018 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[NR3C2]] | B | NR3C2 activity weakens ST7L's drug response | lines that do not express NR3C2 (15) vs lines expressing it (33) | the lines without NR3C2 respond 1.14× as strongly (z diff -0.57); strongest at Ixazomib citrate 5 µM: 0.49x vs 0.72x (z diff -2.1) | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises ST7L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers ST7L's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises ST7L's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without ITPR2-AS1 | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.917). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (2.7, -4.8); signed map (17.8, -25.6). **Vector** length 120, 33.1% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.2 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.7 | +11.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +1.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.7 | -9.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -8.4 | -7.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.0 | -8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -5.2 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -5.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | suppression of tumorigenicity 7 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:112,523,514-112,620,825 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20284, STLR, ST7R, FAM4B |
| Matched by | ensembl_id |

UniProt [Q8TDW4](https://www.uniprot.org/uniprotkb/Q8TDW4) carries no function annotation.

**Summary**, from NCBI Gene [54879](https://www.ncbi.nlm.nih.gov/gene/54879):

> This gene was identified by its similarity to the ST7 tumor suppressor gene found in the chromosome 7q31 region. This gene is clustered in a tail-to-tail manner with the WNT2B gene in a chromosomal region known to be deleted and rearranged in a variety of cancers. Several transcript variants encoding many different isoforms have been described, but some have not been fully characterized. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:18441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18441) · Entrez [54879](https://www.ncbi.nlm.nih.gov/gene/54879) · UniProt [Q8TDW4](https://www.uniprot.org/uniprotkb/Q8TDW4) · Ensembl [ENSG00000007341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007341)

## Data

Gene col 142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 142); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 142]; `tensor/DDL_lfc|DDL_z.npy` [142]; `embed/gene_vectors.npy` [142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 142 or target_col == 142). Every well: [[ST7L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST7L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
