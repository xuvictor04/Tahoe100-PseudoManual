---
symbol: "ATP8A2"
type: "gene"
col: 5391
ensembl_id: "ENSG00000132932"
name: "ATPase phospholipid transporting 8A2"
location: "13q12.13"
module: 165
arm: "+"
pooled_cpm: 3.67
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# ATP8A2

*ATPase phospholipid transporting 8A2* — 13q12.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.57× (z +30.5, q 0e+00, up in 31 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.0732×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.101×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Triamcinolone (drug)]] 0.5 µM in 1 line (H4 0.0738×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.132×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC26]] (+0.77, fdr 7e-06), [[DLGAP2]] (+0.77, fdr 7e-06), [[PTPRT]] (+0.76, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5391.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.57×** | +30.5 | 0e+00 | 31/33 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.39×** | +21.7 | 0e+00 | 37/44 (SNU-423, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.17×** | +17.3 | 0e+00 | 5/5 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +16.0 | 0e+00 | 12/16 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.68×** | +15.2 | 0e+00 | 6/6 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +15.1 | 0e+00 | 26/37 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.08×** | +14.1 | 2e-43 | 29/41 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.91×** | +13.4 | 4e-39 | 26/42 (LoVo, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.82×** | +13.0 | 4e-37 | 28/40 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +9.5 | 1e-19 | 16/38 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.99×** | +8.7 | 2e-16 | 20/45 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.89×** | +8.0 | 6e-14 | 21/44 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +8.0 | 7e-14 | 15/36 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +7.9 | 1e-13 | 14/33 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +6.7 | 7e-10 | 17/44 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.3 | 1e-08 | 11/44 (SW480, A-172, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.001 | 7/42 (SW1417, SW480, …) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.005 | 4/41 (LS 180, SK-MEL-2, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.007 | 2/35 (HT-29, J82) | inconsistent across doses |  |
| [[Sildenafil (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.007 | 1/44 (NCI-H2347) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5391.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.0732×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.101×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Triamcinolone (drug)]] 0.5 µM in 1 line (H4 0.0738×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.132×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.778× | -3.1 | 0.65 | 4/44 (AN3 CA, BT-474, …) | inconsistent across doses |  |
| [[Quinestrol (drug)]] 5 µM |  | 0.842× | -3.0 | 0.65 | 2/44 (HCT15, BT-474) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.95 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 51.4× (z +11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 12.6× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 3.29 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.72× (z +11.2) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0732× (z -10.6) |
| [[LoVo (line)]] | wt | 1.62 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +11.9) | — |
| [[A549 (line)]] | wt | 2.13 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 17.8× (z +10.3) | — |
| [[H4 (line)]] | wt | 9.43 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 16.5× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change | [[Triamcinolone (drug)]] 0.5 µM 0.0738× (z -8.5) |
| [[PANC-1 (line)]] | alt | 1.57 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.51× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 9.42 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.20× (z +12.3) | — |
| [[SW480 (line)]] | alt | 2.21 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 10.3× (z +11.8) | — |
| [[C32 (line)]] | wt | 9.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 3.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC26]] | +0.77 | +0.69 / +0.81 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.77 | +0.61 / +0.84 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.76 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[MTUS2]] | +0.76 | +0.66 / +0.83 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.75 | +0.61 / +0.82 | both halves | 7e-06 |  |
| [[SLC8A1-AS1]] | +0.74 | +0.54 / +0.83 | both halves | 1e-05 |  |
| [[CNTN4]] | +0.73 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[SLC27A6]] | +0.72 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[SGCZ]] | +0.72 | +0.61 / +0.81 | both halves | 7e-06 |  |
| [[FAT3]] | +0.72 | +0.60 / +0.79 | both halves | 7e-06 |  |
| [[HPSE2]] | +0.72 | +0.57 / +0.79 | both halves | 9e-06 |  |
| [[DPP6]] | +0.72 | +0.59 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP8A2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HS6ST3]] | B | HS6ST3 activity raises ATP8A2's level | lines that do not express HS6ST3 (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without HS6ST3 | 0.071 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.872). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.4, 30.4); signed map (31.5, 16.7). **Vector** length 65.6, 9.87% of its response variance represented; |z| ≥ 3 in 1,160 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.8 | +21.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +30.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.1 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +16.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.3 | +15.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.6 | +13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +1.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 8A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.13 — chr13:25,371,974-26,025,851 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATPIB, ML-1 |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTI2](https://www.uniprot.org/uniprotkb/Q9NTI2) (Phospholipid-transporting ATPase IB):

> Catalytic component of a P4-ATPase flippase complex which catalyzes the hydrolysis of ATP coupled to the transport of aminophospholipids from the outer to the inner leaflet of various membranes and ensures the maintenance of asymmetric distribution of phospholipids (By similarity). Able to translocate phosphatidylserine, but not phosphatidylcholine. Phospholipid translocation also seems to be implicated in vesicle formation and in uptake of lipid signaling molecules (By similarity). …

**Summary**, from NCBI Gene [51761](https://www.ncbi.nlm.nih.gov/gene/51761):

> The protein encoded by this gene is a member of the P4 ATPase family of proteins, which are thought to be involved in a process called lipid flipping, whereby phospholipids are translocated inwards from the exoplasmic leaflet to the cytosolic leaflet of the cell membrane, which aids in generating and maintaining asymmetry in membrane lipids. This protein is predicted to contain an E1 E2 ATPase, a haloacid dehalogenase-like hydrolase (HAD) domain, and multiple transmembrane domains. Associations …

**Accessions** — [HGNC:13533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13533) · Entrez [51761](https://www.ncbi.nlm.nih.gov/gene/51761) · UniProt [Q9NTI2](https://www.uniprot.org/uniprotkb/Q9NTI2) · Ensembl [ENSG00000132932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132932)

## Data

Gene col 5391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5391); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5391]; `tensor/DDL_lfc|DDL_z.npy` [5391]; `embed/gene_vectors.npy` [5391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5391 or target_col == 5391). Every well: [[ATP8A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP8A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
