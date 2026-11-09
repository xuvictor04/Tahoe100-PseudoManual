---
symbol: "ADGRF5"
type: "gene"
col: 910
ensembl_id: "ENSG00000069122"
name: "adhesion G protein-coupled receptor F5"
location: "6p12.3"
module: 19
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 11
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ADGRF5

*adhesion G protein-coupled receptor F5* — 6p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.50× (z +11.9, q 1e-29, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.13× (z +10.6, q 4e-24, up in 1 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.559× (z -3.9, q 0.061, down in 2 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 0.199×; ⚠ cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STEAP1B-AS1]] (+0.55, fdr 1e-05), [[SLC4A4]] (+0.53, fdr 1e-05), [[RDH10]] (+0.50, fdr 4e-05); moves opposite to [[SLC25A43]] (-0.44, fdr 3e-04), [[WDR41]] (-0.43, fdr 7e-05), [[ZC2HC1A]] (-0.41, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZC2HC1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 910.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.50×** | +11.9 | 1e-29 | 2/2 (NCI-H2347, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.56×** | +11.3 | 3e-27 | 2/3 (NCI-H2347, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.13×** | +10.6 | 4e-24 | 1/4 (NCI-H2347) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.79×** | +8.1 | 7e-14 | 2/2 (NCI-H2347, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +5.4 | 7e-06 | 1/3 (NCI-H2347) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +4.8 | 1e-04 | 3/7 (SHP-77, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.7 | 2e-04 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.70×** | +4.7 | 2e-04 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +4.2 | 0.002 | 2/4 (NCI-H2347, SHP-77) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +4.1 | 0.002 | 2/7 (NCI-H2347, LOX-IMVI) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +4.0 | 0.003 | 1/6 (Panc 03.27) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +3.8 | 0.007 | 0/3 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.24×** | +3.7 | 0.009 | 1/2 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.12×** | +3.5 | 0.017 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.021 | 0/8 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trimetrexate (drug)]] 0.05 µM |  | **1.64×** | +3.2 | 0.036 | 1/5 (Panc 03.27) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 0.5 µM |  | **1.63×** | +3.2 | 0.042 | 0/6 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +3.2 | 0.042 | 0/7 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.58×** | +3.0 | 0.066 | 0/4 | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.072 | 1/7 (NCI-H2347) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.88×** | +2.9 | 0.073 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.62×** | +2.9 | 0.074 | 0/4 | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.58×** | +2.9 | 0.078 | 0/4 | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.83×** | +2.8 | 0.093 | 0/4 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 910.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 0.199×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.559×** | -3.9 | 0.061 | 2/9 (SHP-77, C-33 A) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.5 µM |  | 0.596× | -3.4 | 0.16 | 1/9 (C-33 A) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.617× | -3.2 | 0.24 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 64.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -11.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.247 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.912 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.712 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.311 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STEAP1B-AS1]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SLC4A4]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[RDH10]] | +0.50 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[BICC1]] | +0.50 | +0.47 / +0.32 | both halves | 2e-04 |  |
| [[CD38]] | +0.49 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[RMDN2-AS1]] | +0.49 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[HAVCR1]] | +0.49 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[COLEC10]] | +0.47 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[IL6]] | +0.46 | +0.43 / +0.44 | both halves | 4e-05 |  |
| [[SFTA3-1]] | +0.46 | +0.56 / +0.24 | both halves | 4e-04 |  |
| [[NTNG2]] | +0.46 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[LINC02882]] | +0.46 | +0.48 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A43]] | -0.44 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[WDR41]] | -0.43 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[ZC2HC1A]] | -0.41 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[NOD1]] | -0.40 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[CLTCL1]] | -0.38 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[STARD9]] | -0.38 | -0.39 / -0.24 | both halves | 4e-04 |  |
| [[PPP2R2C]] | -0.38 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[ZNF600]] | -0.36 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[PARP16]] | -0.36 | -0.14 / -0.39 | ⚠ not reproduced | 0.002 |  |
| [[FNBP1L]] | -0.36 | -0.23 / -0.37 | both halves | 6e-04 |  |
| [[PRKCD]] | -0.35 | -0.27 / -0.31 | both halves | 3e-04 |  |
| [[ANKRD36B]] | -0.35 | -0.30 / -0.28 | both halves | 3e-04 |  |
| [[SLC66A3]] | -0.35 | -0.32 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADGRF5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC2HC1A]] | B | ADGRF5 activity raises ZC2HC1A's level | lines that do not express ADGRF5 (39) vs lines expressing it (11) | 1.37× lower at baseline in the lines without ADGRF5 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01425, OVAAL, LINC02267 |
| [[GALNT5]] | C | ADGRF5 activity raises GALNT5's level | lines that do not express ADGRF5 (39) vs lines expressing it (11) | 1.54× lower at baseline in the lines without ADGRF5 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01425, OVAAL, LINC02267; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.218). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.8, 23.4); signed map (50.6, 27.2). **Vector** length 15.9, 3.58% of its response variance represented; |z| ≥ 3 in 155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +4.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.0 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.4 | +1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.4 | +0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.4 | -0.6 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.6 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.5 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.5 | -0.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.4 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor F5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.3 — chr6:46,852,522-46,954,943 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564O1923, KIAA0758; previously GPR116 |
| Gene groups (HGNC) | I-set domain containing; Immunoglobulin like domain containing; Adhesion G protein-coupled receptors, subfamily F; SEA domain containing |
| Reactome | 1 pathways, smallest: Surfactant metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZF2](https://www.uniprot.org/uniprotkb/Q8IZF2) (Adhesion G protein-coupled receptor F5):

> Adhesion G protein-coupled receptor. In alveolar type II (ATII or AT2) cells, required for normal lung surfactant homeostasis. Modulation of both surfactant secretion and uptake by ATII cells is mediated by the downstream activation of GNAQ/GNA11 proteins and may be a consequence of increased cortical F-actin assembly induced by ADGRF5 activation. In the kidney, may play a role in the regulation of acid excretion into the primary urine, possibly by regulating the surface expression of V-ATPase …

**Summary**, from NCBI Gene [221395](https://www.ncbi.nlm.nih.gov/gene/221395):

> Predicted to enable G protein-coupled receptor activity. Predicted to be involved in several processes, including adenylate cyclase-activating G protein-coupled receptor signaling pathway; glucose homeostasis; and surfactant homeostasis. Predicted to act upstream of or within several processes, including glomerular filtration; negative regulation of macrophage activation; and pharyngeal arch artery morphogenesis. Located in cell surface and cytoplasmic vesicle. [provided by Alliance of Genome …

**Accessions** — [HGNC:19030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19030) · Entrez [221395](https://www.ncbi.nlm.nih.gov/gene/221395) · UniProt [Q8IZF2](https://www.uniprot.org/uniprotkb/Q8IZF2) · Ensembl [ENSG00000069122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069122)

## Data

Gene col 910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 910); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 910]; `tensor/DDL_lfc|DDL_z.npy` [910]; `embed/gene_vectors.npy` [910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 910 or target_col == 910). Every well: [[ADGRF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
