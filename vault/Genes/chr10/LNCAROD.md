---
symbol: "LNCAROD"
type: "gene"
col: 13780
ensembl_id: "ENSG00000231131"
name: "lncRNA activating regulator of DKK1"
location: "10q21.1"
module: 27
arm: "+"
pooled_cpm: 16.84
n_lines_expressing: 16
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# LNCAROD

*lncRNA activating regulator of DKK1* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.70× (z +16.4, q 0e+00, up in 6 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.50× (z +13.7, q 1e-40, up in 3 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.679× (z -4.1, q 0.010, down in 9 of 13 measured lines).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEG3]] (+0.68, fdr 7e-06), [[LRRTM4]] (+0.63, fdr 1e-05), [[APOB]] (+0.63, fdr 1e-04); moves opposite to [[KANSL3]] (-0.35, fdr 8e-04, ⚠ not reproduced), [[GNE]] (-0.34, fdr 4e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC00470]] → it (grade C ⚠); 4 go from it, the strongest it → [[LINC01205]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.70×** | +16.4 | 0e+00 | 6/12 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.45×** | +15.2 | 0e+00 | 3/7 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +13.7 | 1e-40 | 3/13 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +9.6 | 7e-20 | 3/9 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.97×** | +7.2 | 7e-11 | 1/12 (BT-474) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.73×** | +5.8 | 5e-07 | 3/13 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +4.3 | 0.001 | 2/13 (NCI-H1573, LoVo) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.002 | 1/12 (MIA PaCa-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.003 | 2/13 (BT-474, AN3 CA) | rises with dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.44×** | +3.6 | 0.020 | 7/13 (NCI-H1573, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13780.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.679×** | -4.1 | 0.010 | 9/13 (A-427, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.680×** | -4.1 | 0.010 | 3/13 (COLO 205, A-172, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **0.762×** | -4.0 | 0.010 | 5/13 (HepG2/C3A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.687×** | -4.0 | 0.011 | 0/13 | rises with dose |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.715× | -3.3 | 0.12 | 0/13 | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.736× | -3.2 | 0.12 | 1/13 (SW 900) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 295 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0391× (z -18.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -9.5) |
| [[A-172 (line)]] | wt | 230 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 9.39 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.83× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 97.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -11.3) |
| [[AN3 CA (line)]] | alt | 89.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0963× (z -9.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 5.92 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0649× (z -8.5) |
| [[LoVo (line)]] | wt | 6.11 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.90× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 50.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -8.9) |
| [[NCI-H661 (line)]] | alt | 97.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0410× (z -10.4) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 22 of them with an alert (⚠; 22 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEG3]] | +0.68 | +0.66 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[LRRTM4]] | +0.63 | +0.56 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[APOB]] | +0.63 | +0.68 / +0.36 | both halves | 1e-04 | **novel candidate** |
| [[LINC02008]] | +0.53 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[UNC5C]] | +0.50 | +0.37 / +0.47 | both halves | 9e-05 |  |
| [[SUCNR1]] | +0.48 | +0.33 / +0.39 | both halves | 1e-04 |  |
| [[DMD]] | +0.47 | +0.21 / +0.47 | both halves | 6e-04 |  |
| [[TTTY10]] | +0.47 | +0.51 / +0.42 | both halves | 4e-05 | same gene group |
| [[AFP]] | +0.47 | +0.62 / +0.05 | ⚠ one half (not replicated) | 0.005 |  |
| [[SOX5]] | +0.44 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[PHYHIPL]] | +0.44 | +0.43 / +0.33 | both halves | 1e-04 |  |
| [[LINC00470]] | +0.43 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[TAFA5]] | +0.43 | +0.42 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANSL3]] | -0.35 | -0.36 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[GNE]] | -0.34 | -0.26 / -0.29 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00470]] | C | LINC00470 activity raises LNCAROD's level | lines that do not express LINC00470 (38) vs lines expressing it (12) | 3.45× lower at baseline in the lines without LINC00470 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, ENSG00000287474, FCRLA; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises LNCAROD's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 3.82× lower at baseline in the lines without GABRG2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LINC01205]] | C | LINC01205 activity raises LNCAROD's level | lines that do not express LINC01205 (44) vs lines expressing it (6) | 4.41× lower at baseline in the lines without LINC01205 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, ENSG00000241168, GPR15; maybe low, not absent; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises LNCAROD's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 3.19× lower at baseline in the lines without CCDC144NL-AS1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[AXIN2]] | C | AXIN2 activity raises LNCAROD's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.31× lower at baseline in the lines without AXIN2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises LNCAROD's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without LOXL3 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01205]] | C | LNCAROD activity raises LINC01205's level | lines that do not express LNCAROD (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without LNCAROD | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000260573, AFP, LINC02566; maybe low, not absent; co-absent with the target |
| [[LINC01203]] | C | LNCAROD activity raises LINC01203's level | lines that do not express LNCAROD (34) vs lines expressing it (16) | 1.46× lower at baseline in the lines without LNCAROD | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000260573, AFP, LINC02566; maybe low, not absent; co-absent with the target |
| [[AXIN2]] | C | LNCAROD activity raises AXIN2's level | lines that do not express LNCAROD (34) vs lines expressing it (16) | 1.96× lower at baseline in the lines without LNCAROD | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000260573, AFP, LINC02566; maybe low, not absent; co-absent with the target |
| [[LINC00470]] | C | LNCAROD activity raises LINC00470's level | lines that do not express LNCAROD (34) vs lines expressing it (16) | 2.77× lower at baseline in the lines without LNCAROD | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000260573, AFP, LINC02566; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.315). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.9, 53.9); signed map (65.3, 19.8). **Vector** length 39.4, 10.2% of its response variance represented; |z| ≥ 3 in 335 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.6 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +13.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.8 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | +2.5 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -4.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | lncRNA activating regulator of DKK1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q21.1 — chr10:52,450,874-52,755,509 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lnc-MBL2-4, A-ROD; previously LINC01468 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50913) · Entrez [101928687](https://www.ncbi.nlm.nih.gov/gene/101928687) · Ensembl [ENSG00000231131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231131)

## Data

Gene col 13780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13780); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13780]; `tensor/DDL_lfc|DDL_z.npy` [13780]; `embed/gene_vectors.npy` [13780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13780 or target_col == 13780). Every well: [[LNCAROD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LNCAROD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
