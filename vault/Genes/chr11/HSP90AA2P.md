---
symbol: "HSP90AA2P"
type: "gene"
col: 13397
ensembl_id: "ENSG00000224411"
name: "heat shock protein 90 alpha family class A member 2, pseudogene"
location: "11p14.1"
module: 60
arm: "+"
pooled_cpm: 2.94
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSP90AA2P

*heat shock protein 90 alpha family class A member 2, pseudogene* — 11p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (18 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 13.4× (z +22.0, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.855× (z -4.8, q 1e-03, down in 20 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Rifaximin (drug)]] 5 µM: 0.580× (z -4.5, q 0.002, down in 12 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[LJI308 (drug)]] 0.05 µM in 1 line (KATO III 0.0595×); [[Demeclocycline (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0552×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90AB3P]] (+0.85, fdr 7e-06), [[HSP90AA1]] (+0.83, fdr 7e-06), [[HSP90AB2P]] (+0.79, fdr 7e-06); moves opposite to [[DOP1A]] (-0.58, fdr 1e-05), [[YY1AP1]] (-0.58, fdr 1e-05), [[TNRC6C]] (-0.52, fdr 9e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPX3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **13.4×** | +22.0 | 0e+00 | 40/40 (SW480, HEC-1-A, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **13.3×** | +21.9 | 0e+00 | 41/41 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **10.9×** | +20.2 | 0e+00 | 43/43 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **8.48×** | +17.1 | 0e+00 | 39/39 (NCI-H2347, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **5.89×** | +15.0 | 0e+00 | 12/14 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **6.29×** | +14.9 | 0e+00 | 5/5 (HOP62, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.66×** | +12.0 | 2e-31 | 9/9 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **9.30×** | +9.9 | 5e-21 | 8/9 (NCI-H2347, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **4.85×** | +9.5 | 1e-19 | 35/42 (NCI-H2347, CFPAC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **2.57×** | +7.7 | 1e-12 | 13/22 (HEC-1-A, SW 900, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **5.01×** | +7.1 | 6e-11 | 20/29 (NCI-H2347, SW480, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **2.23×** | +6.7 | 8e-10 | 5/19 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.03×** | +5.9 | 1e-07 | 23/46 (SW480, HOP62, …) | rises with dose | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.10×** | +4.4 | 4e-04 | 4/5 (NCI-H2347, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.69×** | +4.4 | 4e-04 | 17/42 (HOP62, SW480, …) | rises with dose | position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | **2.64×** | +4.3 | 6e-04 | 5/35 (KATO III, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.65×** | +4.0 | 0.002 | 10/40 (NCI-H460, HOP62, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.012 | 8/42 (HOP62, NCI-H460, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.016 | 2/43 (KATO III, SW480) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +2.9 | 0.073 | 2/43 (NCI-H1792, HOP62) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +2.9 | 0.079 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13397.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[LJI308 (drug)]] 0.05 µM in 1 line (KATO III 0.0595×); [[Demeclocycline (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0552×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.855× | -4.8 | 1e-03 | 20/48 (MIA PaCa-2, BT-474, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | **0.580×** | -4.5 | 0.002 | 12/39 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.645×** | -3.8 | 0.032 | 8/45 (A-427, LS 180, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.683× | -3.3 | 0.15 | 7/45 (RPMI-7951, SNU-1, …) | two highest doses |  |
| [[Rifaximin (drug)]] 0.5 µM |  | 0.706× | -3.0 | 0.26 | 10/44 (HepG2/C3A, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 4.95 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 18.2× (z +13.3) | — |
| [[NCI-H2347 (line)]] | alt | 5.33 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 14.1× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 2.79 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 20.6× (z +9.1) | [[Demeclocycline (drug)]] 0.5 µM 0.0552× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 3.00 | 3 | 0 | [[Auranofin (drug)]] 5 µM 22.6× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 2.71 | 3 | 0 | [[Auranofin (drug)]] 5 µM 30.9× (z +10.3) | — |
| [[KATO III (line)]] | alt | 3.76 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 14.6× (z +8.8) | [[LJI308 (drug)]] 0.05 µM 0.0595× (z -8.8) |
| [[A498 (line)]] | wt | 1.82 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 14.1× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 4.47 | 1 | 0 | [[Auranofin (drug)]] 5 µM 18.9× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 1.63 | 1 | 0 | [[Auranofin (drug)]] 5 µM 36.8× (z +8.8) | — |
| [[LoVo (line)]] | wt | 2.13 | 1 | 0 | [[Auranofin (drug)]] 5 µM 22.8× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 3.33 | 1 | 0 | [[Auranofin (drug)]] 5 µM 20.8× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 2.62 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 19.5× (z +8.6) | — |
| [[A-172 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90AB3P]] | +0.85 | +0.82 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[HSP90AA1]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[HSP90AB2P]] | +0.79 | +0.78 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CACYBP]] | +0.78 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[HSPE1]] | +0.77 | +0.77 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[HSPA1B]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SOD1]] | +0.74 | +0.82 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[VCP]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SERPINH1]] | +0.71 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[HSPA8]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CCT4]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[STIP1]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1A]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.52 | -0.60 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPX3]] | B | GPX3 activity lowers HSP90AA2P's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.24× higher at baseline in the lines without GPX3 | 0.0999 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.922). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.2, -11.0); signed map (-26.0, -28.5). **Vector** length 75.9, 13.7% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *heat shock* (control, mean cos +0.65 to 13); *Attenuation phase* (reactome, mean cos +0.65 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.63 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.3 | +22.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.7 | +21.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.5 | +17.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.3 | +20.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.5 | +9.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.4 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -0.0 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -3.3 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein 90 alpha family class A member 2, pseudogene |
| Locus type | pseudogene |
| Location | 11p14.1 — chr11:27,888,838-27,891,033 (-) |
| Ensembl biotype | processed_pseudogene |
| Also known as | HSPCA, HSP90ALPHA; previously HSPCAL3, HSP90AA2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14568](https://www.uniprot.org/uniprotkb/Q14568) (Heat shock protein HSP 90-alpha A2):

> Putative molecular chaperone that may promote the maturation, structural maintenance and proper regulation of specific target proteins.

**Summary**, from NCBI Gene [3324](https://www.ncbi.nlm.nih.gov/gene/3324):

> HSP90 proteins are highly conserved molecular chaperones that have key roles in signal transduction, protein folding, protein degradation, and morphologic evolution. HSP90 proteins normally associate with other cochaperones and play important roles in folding newly synthesized proteins or stabilizing and refolding denatured proteins after stress. HSP90AA2 is a cytosolic HSP90 protein. Other HSP90 proteins are found in endoplasmic reticulum (HSP90B1; MIM 191175) and mitochondria (TRAP1; MIM …

**Accessions** — [HGNC:5256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5256) · Entrez [3324](https://www.ncbi.nlm.nih.gov/gene/3324) · UniProt [Q14568](https://www.uniprot.org/uniprotkb/Q14568) · Ensembl [ENSG00000224411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224411)

## Data

Gene col 13397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13397); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13397]; `tensor/DDL_lfc|DDL_z.npy` [13397]; `embed/gene_vectors.npy` [13397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13397 or target_col == 13397). Every well: [[HSP90AA2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSP90AA2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
