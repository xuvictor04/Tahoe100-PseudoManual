---
symbol: "TMEM234"
type: "gene"
col: 8293
ensembl_id: "ENSG00000160055"
name: "transmembrane protein 234"
location: "1p35.2"
module: 89
arm: "+"
pooled_cpm: 6.0
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# TMEM234

*transmembrane protein 234* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.24× (z +9.7, q 2e-19, up in 25 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.41× (z +4.0, q 0.010, up in 12 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.604× (z -8.8, q 6e-16, down in 32 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.153×; ⚠ cell-cycle shift, explains ~79% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SHP-77 0.0860×; ⚠ toxic; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0972×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Bergenin (drug)]] 0.5 µM in 1 line (RKO 0.0706×); [[Decitabine (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0705×); [[Naproxen (drug)]] 0.05 µM in 1 line (A-427 0.0684×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCTN2]] (+0.63, fdr 1e-05), [[POLL]] (+0.62, fdr 7e-06), [[ALKBH3]] (+0.59, fdr 1e-05); moves opposite to [[RNF157]] (-0.51, fdr 7e-05), [[MT1A]] (-0.51, fdr 1e-04), [[TLL2]] (-0.47, fdr 4e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +9.7 | 2e-19 | 25/48 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.28×** | +4.4 | 0.003 | 14/47 (LoVo, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.010 | 12/43 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.026 | 12/44 (A-172, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.28× | +3.1 | 0.17 | 3/45 (NCI-H23, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | 1.28× | +3.1 | 0.17 | 8/44 (SW480, H4, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.17 | 5/44 (J82, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8293.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.153×; ⚠ cell-cycle shift, explains ~79% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SHP-77 0.0860×; ⚠ toxic; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0972×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Bergenin (drug)]] 0.5 µM in 1 line (RKO 0.0706×); [[Decitabine (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0705×); [[Naproxen (drug)]] 0.05 µM in 1 line (A-427 0.0684×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.604×** | -8.8 | 6e-16 | 32/46 (MIA PaCa-2, J82, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.587×** | -6.2 | 2e-07 | 20/35 (SHP-77, RKO, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.717×** | -5.8 | 1e-06 | 22/39 (NCI-H23, SNU-423, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.669×** | -5.0 | 9e-05 | 22/47 (LS 180, HOP62, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.677×** | -4.8 | 1e-04 | 20/44 (SW48, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.699×** | -4.4 | 9e-04 | 18/41 (HOP62, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.708×** | -4.0 | 0.005 | 15/44 (COLO 205, NCI-H460, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.764×** | -3.3 | 0.059 | 12/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.765× | -3.1 | 0.12 | 7/47 (CHP-212, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.49 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0684× (z -9.3) |
| [[A549 (line)]] | wt | 5.52 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0829× (z -8.8) |
| [[COLO 205 (line)]] | alt | 8.89 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0479× (z -10.2) ⚠ cell-cycle shift, explains ~67% of this change |
| [[Hs 766T (line)]] | wt | 6.95 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 5 µM 0.215× (z -8.8) |
| [[HS-578T (line)]] | alt | 8.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.83 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0972× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 4.55 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0705× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 7.66 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -12.0) ⚠ cell-cycle shift, explains ~79% of this change |
| [[RKO (line)]] | wt | 5.84 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0706× (z -9.7) |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0860× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 7.12 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCTN2]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[POLL]] | +0.62 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ALKBH3]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[GPALPP1]] | +0.57 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[RABL2A]] | +0.57 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[VPS33A]] | +0.56 | +0.36 / +0.59 | both halves | 1e-04 |  |
| [[POLR3F]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[SUPT7L]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[WDR73]] | +0.55 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[APH1A]] | +0.54 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[SNX21]] | +0.54 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[WDR83]] | +0.54 | +0.41 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF157]] | -0.51 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[MT1A]] | -0.51 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[TLL2]] | -0.47 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[KIAA1958]] | -0.47 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[IL3RA]] | -0.47 | -0.26 / -0.59 | both halves | 4e-04 |  |
| [[SEMA6B]] | -0.47 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[LINC00937]] | -0.46 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[EGR3]] | -0.44 | -0.44 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TMEM234's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.1, 7.8); signed map (-9.1, -17.0). **Vector** length 51.8, 6.43% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +3.0 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.6 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | +0.4 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 234 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:32,214,472-32,222,359 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RP4-622L5, dJ622L5.7, FLJ90779; previously C1orf91 |
| Matched by | ensembl_id |

UniProt [Q8WY98](https://www.uniprot.org/uniprotkb/Q8WY98) carries no function annotation.

**Summary**, from NCBI Gene [56063](https://www.ncbi.nlm.nih.gov/gene/56063):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28837) · Entrez [56063](https://www.ncbi.nlm.nih.gov/gene/56063) · UniProt [Q8WY98](https://www.uniprot.org/uniprotkb/Q8WY98) · Ensembl [ENSG00000160055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160055)

## Data

Gene col 8293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8293); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8293]; `tensor/DDL_lfc|DDL_z.npy` [8293]; `embed/gene_vectors.npy` [8293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8293 or target_col == 8293). Every well: [[TMEM234 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM234.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
