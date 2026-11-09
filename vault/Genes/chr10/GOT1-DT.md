---
symbol: "GOT1-DT"
type: "gene"
col: 13432
ensembl_id: "ENSG00000224934"
name: "GOT1 divergent transcript"
location: "10q24.2"
module: 15
arm: "+"
pooled_cpm: 2.8
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# GOT1-DT

*GOT1 divergent transcript* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.78× (z +22.3, q 0e+00, up in 33 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.558× (z -5.3, q 8e-05, down in 18 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.141×; ⚠ toxic; transcription drop); [[Pimozide (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0892×); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Elagolix sodium (drug)]] 0.05 µM in 1 line (SHP-77 0.0785×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS13B-DT]] (+0.83, fdr 7e-06), [[LINC00115]] (+0.77, fdr 1e-05), [[CAPN10-DT]] (+0.73, fdr 3e-05); moves opposite to [[NEK1]] (-0.58, fdr 1e-04), [[VCL]] (-0.57, fdr 3e-05), [[WDR7]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01139]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.78×** | +22.3 | 0e+00 | 33/33 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **4.38×** | +12.8 | 6e-35 | 13/16 (NCI-H1573, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.08×** | +9.3 | 2e-18 | 20/44 (A549, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +8.8 | 2e-16 | 22/33 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +8.1 | 6e-14 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +7.9 | 3e-13 | 10/26 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.36×** | +7.7 | 8e-13 | 25/45 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +7.4 | 1e-11 | 1/4 (Hs 766T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.13×** | +6.8 | 6e-10 | 21/44 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +6.4 | 7e-09 | 4/11 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.98×** | +6.2 | 4e-08 | 20/44 (LoVo, H4, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +5.3 | 5e-06 | 11/43 (A498, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.6 | 2e-04 | 12/44 (A-172, HOP62, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.63×** | +4.4 | 5e-04 | 6/46 (KATO III, NCI-H1573, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.3 | 6e-04 | 7/34 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.002 | 12/39 (A-427, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +3.1 | 0.051 | 6/45 (A-172, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.084 | 3/44 (A-172, SW1417, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +2.9 | 0.094 | 0/39 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.094 | 4/40 (CFPAC-1, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13432.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.141×; ⚠ toxic; transcription drop); [[Pimozide (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0892×); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.176×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Elagolix sodium (drug)]] 0.05 µM in 1 line (SHP-77 0.0785×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.558×** | -5.3 | 8e-05 | 18/41 (HepG2/C3A, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.626×** | -4.1 | 0.010 | 17/40 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.638×** | -4.0 | 0.010 | 14/41 (PANC-1, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.32 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.08× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.47× (z +10.6) | — |
| [[A498 (line)]] | wt | 1.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.58× (z +9.8) | — |
| [[A549 (line)]] | wt | 1.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 3.81 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0892× (z -9.4) |
| [[HOP62 (line)]] | alt | 2.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 1.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.6× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 1.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.42× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 3.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 4.78 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.05 µM 0.0785× (z -8.5) |
| [[SNU-423 (line)]] | alt | 2.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.22× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 2.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +9.0) | — |
| [[A-427 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS13B-DT]] | +0.83 | +0.79 / +0.77 | both halves | 7e-06 | same gene group |
| [[LINC00115]] | +0.77 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[CAPN10-DT]] | +0.73 | +0.46 / +0.77 | both halves | 3e-05 | same gene group |
| [[SDHAF4]] | +0.72 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MIR762HG]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[HLA-DMA]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CCNY-AS1]] | +0.68 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ZNF460-AS1]] | +0.66 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[SEC24B-AS1]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ACTG1P17]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK1]] | -0.58 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[VCL]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[WDR7]] | -0.56 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[CLEC16A]] | -0.56 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[RABGAP1L]] | -0.54 | -0.47 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01139]] | B | LINC01139 activity raises GOT1-DT's level | lines that do not express LINC01139 (24) vs lines expressing it (26) | 1.32× lower at baseline in the lines without LINC01139 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, NTRK3, CTNNA2 |
| [[TOP2A]] | B | TOP2A activity lowers GOT1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.777). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.9, 23.3); signed map (1.5, -0.3). **Vector** length 56.7, 8.20% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +22.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +6.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -3.2 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | GOT1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q24.2 — chr10:99,430,915-99,463,259 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55848) · Entrez [101927300](https://www.ncbi.nlm.nih.gov/gene/101927300) · Ensembl [ENSG00000224934](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224934)

## Data

Gene col 13432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13432); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13432]; `tensor/DDL_lfc|DDL_z.npy` [13432]; `embed/gene_vectors.npy` [13432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13432 or target_col == 13432). Every well: [[GOT1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOT1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
