---
symbol: "GRM7"
type: "gene"
col: 12170
ensembl_id: "ENSG00000196277"
name: "glutamate metabotropic receptor 7"
location: "3p26.1"
module: 90
arm: "+"
pooled_cpm: 4.46
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# GRM7

*glutamate metabotropic receptor 7* — 3p26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.88× (z +20.1, q 0e+00, up in 23 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.179×; ⚠ toxic; transcription drop); [[Peretinoin (drug)]] 5 µM in 1 line (H4 0.0559×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.255×; ⚠ toxic; transcription drop); [[Bortezomib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0589×); [[Harringtonine (drug)]] 0.05 µM in 1 line (H4 0.0843×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[G2E3-AS1]] (+0.82, fdr 7e-06), [[CLVS1]] (+0.81, fdr 7e-06), [[LINC02208]] (+0.80, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SPINK5]] → it (grade B ⚠); 4 go from it, the strongest it → [[C2CD5-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.88×** | +20.1 | 0e+00 | 23/31 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.63×** | +13.5 | 5e-39 | 9/13 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +11.5 | 4e-28 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +11.3 | 2e-27 | 20/35 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.36×** | +9.0 | 3e-17 | 24/41 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +8.8 | 2e-16 | 25/44 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +6.7 | 2e-09 | 2/4 (LS 180, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +5.7 | 1e-06 | 12/38 (SHP-77, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +5.5 | 2e-06 | 6/43 (LS 180, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +5.5 | 2e-06 | 1/11 (NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.3 | 5e-06 | 7/22 (SHP-77, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.0 | 2e-05 | 8/33 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +4.3 | 6e-04 | 10/38 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.3 | 6e-04 | 6/27 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.3 | 7e-04 | 5/21 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +4.2 | 8e-04 | 14/39 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.001 | 8/43 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +3.5 | 0.016 | 0/25 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.041 | 6/33 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.060 | 2/40 (NCI-H23, RPMI-7951) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 0.5 µM |  | **1.32×** | +2.9 | 0.082 | 1/41 (Hs 766T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12170.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.179×; ⚠ toxic; transcription drop); [[Peretinoin (drug)]] 5 µM in 1 line (H4 0.0559×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.255×; ⚠ toxic; transcription drop); [[Bortezomib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0589×); [[Harringtonine (drug)]] 0.05 µM in 1 line (H4 0.0843×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.875× | -5.1 | 2e-04 | 20/47 (A549, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 100 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -11.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 19.6 | 0 | 2 | — | [[Peretinoin (drug)]] 5 µM 0.0559× (z -10.8) |
| [[C-33 A (line)]] | alt | 7.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 1.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.18× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 1 | — | [[Bortezomib (drug)]] 0.5 µM 0.0589× (z -8.9) |
| [[A-172 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[G2E3-AS1]] | +0.82 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.81 | +0.64 / +0.84 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.80 | +0.61 / +0.82 | both halves | 7e-06 |  |
| [[DPP6]] | +0.78 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.77 | +0.56 / +0.79 | both halves | 1e-05 |  |
| [[GRM8]] | +0.77 | +0.66 / +0.74 | both halves | 7e-06 | pathway: Class C/3 (Metabotropic glutamate/pheromone receptors); STRING 936 |
| [[CNTNAP5]] | +0.77 | +0.61 / +0.83 | both halves | 7e-06 |  |
| [[DLEU7]] | +0.76 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[LINC02694]] | +0.76 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[USH2A]] | +0.75 | +0.57 / +0.80 | both halves | 9e-06 |  |
| [[PPP1R9A-AS1]] | +0.75 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[LINC01414]] | +0.75 | +0.58 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINK5]] | B | SPINK5 activity raises GRM7's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 2.14× lower at baseline in the lines without SPINK5 | 0.014 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[TOP2A]] | B | TOP2A activity lowers GRM7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRRTM4]] | B | LRRTM4 activity raises GRM7's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.14× lower at baseline in the lines without LRRTM4 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[LINC02147]] | B | LINC02147 activity raises GRM7's level | lines that do not express LINC02147 (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without LINC02147 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC00992, PROX1-AS1, MOGAT3; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2CD5-AS1]] | C | GRM7's natural level weakens C2CD5-AS1's drug response | GRM7's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.12; direction clear | 0.069 | ⚠ tissue can mimic it; precision caveat |
| [[CLVS1]] | C | GRM7's natural level weakens CLVS1's drug response | GRM7's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.51; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CNBD1]] | C | GRM7's natural level weakens CNBD1's drug response | GRM7's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.44; direction not clear | 0.085 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PTPRT]] | C | GRM7's natural level weakens PTPRT's drug response | GRM7's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.51; direction not clear | 0.085 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.862). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.1, 28.2); signed map (34.5, 14.0). **Vector** length 50.9, 6.69% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +20.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +0.6 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -2.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -5.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | glutamate metabotropic receptor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.1 — chr3:6,770,001-7,741,533 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GLUR7, GPRC1G, mGlu7, MGLUR7, PPP1R87 |
| Gene groups (HGNC) | Glutamate metabotropic receptors; Protein phosphatase 1 regulatory subunits |
| Reactome | 5 pathways, smallest: Class C/3 (Metabotropic glutamate/pheromone receptors); G alpha (i) signalling events; GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14831](https://www.uniprot.org/uniprotkb/Q14831) (Metabotropic glutamate receptor 7):

> G protein-coupled receptor activated by glutamate that regulates axon outgrowth through the MAPK-cAMP-PKA signaling pathway during neuronal development. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase that it inhibits.

**Summary**, from NCBI Gene [2917](https://www.ncbi.nlm.nih.gov/gene/2917):

> L-glutamate is the major excitatory neurotransmitter in the central nervous system, and it activates both ionotropic and metabotropic glutamate receptors. Glutamatergic neurotransmission is involved in most aspects of normal brain function and can be perturbed in many neuropathologic conditions. The metabotropic glutamate receptors are a family of G protein-coupled receptors that have been divided into three groups on the basis of sequence homology, putative signal transduction mechanisms, and …

**Accessions** — [HGNC:4599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4599) · Entrez [2917](https://www.ncbi.nlm.nih.gov/gene/2917) · UniProt [Q14831](https://www.uniprot.org/uniprotkb/Q14831) · Ensembl [ENSG00000196277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196277)

## Data

Gene col 12170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12170); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12170]; `tensor/DDL_lfc|DDL_z.npy` [12170]; `embed/gene_vectors.npy` [12170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12170 or target_col == 12170). Every well: [[GRM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
