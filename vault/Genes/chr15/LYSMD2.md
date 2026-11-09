---
symbol: "LYSMD2"
type: "gene"
col: 6384
ensembl_id: "ENSG00000140280"
name: "LysM domain containing 2"
location: "15q21.2"
module: 70
arm: "+"
pooled_cpm: 4.3
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# LYSMD2

*LysM domain containing 2* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.66× (z +7.8, q 4e-12, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.687× (z -4.1, q 0.023, down in 11 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.123×, LoVo 0.152×, NCI-H2030 0.249×; ⚠ cell-cycle shift, explains ~15% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (RKO 0.0623×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tadalafil (drug)]] 5 µM in 1 line (A549 0.0677×); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (A-427 0.0840×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIBAR1]] (+0.61, fdr 1e-05), [[LYN]] (+0.61, fdr 3e-05), [[ZNF618]] (+0.59, fdr 1e-05); moves opposite to [[PPP1R13L]] (-0.45, fdr 7e-05), [[ATP6V1D]] (-0.45, fdr 4e-05), [[RECQL5]] (-0.44, fdr 2e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARHGAP44]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6384.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +7.8 | 4e-12 | 25/44 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +6.4 | 4e-08 | 11/21 (LS 180, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.72×** | +5.9 | 9e-07 | 9/19 (NCI-H1792, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +5.8 | 1e-06 | 19/41 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.0 | 7e-05 | 5/47 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.9 | 9e-05 | 8/25 (LS 180, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +4.5 | 5e-04 | 12/45 (NCI-H1792, J82, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.34×** | +4.5 | 5e-04 | 13/35 (A549, NCI-H460, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.34×** | +4.5 | 5e-04 | 8/44 (RPMI-7951, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.55×** | +4.4 | 5e-04 | 1/5 (CFPAC-1) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.001 | 9/45 (PANC-1, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.005 | 6/44 (NCI-H1792, C32, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.6 | 0.015 | 6/34 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.42×** | +3.5 | 0.020 | 2/7 (PANC-1, CFPAC-1) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.044 | 12/45 (NCI-H2347, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.056 | 2/30 (SW480, NCI-H1573) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.074 | 6/43 (AsPC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6384.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.123×, LoVo 0.152×, NCI-H2030 0.249×; ⚠ cell-cycle shift, explains ~15% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (RKO 0.0623×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tadalafil (drug)]] 5 µM in 1 line (A549 0.0677×); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (A-427 0.0840×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.687×** | -4.1 | 0.023 | 11/42 (C32, HS-578T, …) | two highest doses | low cells (technical?); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.787×** | -3.7 | 0.054 | 15/44 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.747× | -3.2 | 0.13 | 4/45 (H4, NCI-H460, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.815× | -3.2 | 0.13 | 10/44 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.573× | -3.2 | 0.13 | 6/41 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.816× | -3.2 | 0.13 | 8/45 (C-33 A, HCT15, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.738× | -3.1 | 0.13 | 7/45 (HT-29, AN3 CA, …) | inconsistent across doses |  |
| [[Baicalin (drug)]] 0.5 µM |  | 0.753× | -3.1 | 0.13 | 3/43 (COLO 205, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.745× | -3.0 | 0.15 | 11/38 (NCI-H2030, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~13% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 9.15 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.0) ⚠ cell-cycle shift, explains ~15% of this change |
| [[A-427 (line)]] | wt | 3.97 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0840× (z -8.8) |
| [[A498 (line)]] | wt | 8.32 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -16.4) ⚠ cell-cycle shift, explains ~15% of this change |
| [[A549 (line)]] | wt | 4.72 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0677× (z -9.0) |
| [[LoVo (line)]] | wt | 8.06 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -13.2) ⚠ cell-cycle shift, explains ~15% of this change |
| [[RKO (line)]] | wt | 6.99 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0623× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 3.44 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +8.5) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[A-172 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIBAR1]] | +0.61 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[LYN]] | +0.61 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[ZNF618]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CD5L]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[IL15RA]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PARP12]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PYURF]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[APOL3]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[TMEM98]] | +0.53 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[ZNF174]] | +0.52 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TAP2]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[SLC18B1]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R13L]] | -0.45 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[ATP6V1D]] | -0.45 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RECQL5]] | -0.44 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[MFSD11]] | -0.44 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[DYNC2I1]] | -0.44 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[CYTH2]] | -0.43 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[MAP3K7]] | -0.43 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ACOX3]] | -0.42 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[RAPGEF6]] | -0.42 | -0.56 / -0.24 | both halves | 4e-04 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP44]] | B | ARHGAP44 activity raises LYSMD2's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.55× lower at baseline in the lines without ARHGAP44 | 0.074 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.417). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.5, 53.6); signed map (52.4, -2.0). **Vector** length 54.3, 7.68% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -2.6 | -1.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | -1.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | LysM domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:51,723,011-51,751,585 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35274 |
| Gene groups (HGNC) | LysM domain containing |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

UniProt [Q8IV50](https://www.uniprot.org/uniprotkb/Q8IV50) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28571) · Entrez [256586](https://www.ncbi.nlm.nih.gov/gene/256586) · UniProt [Q8IV50](https://www.uniprot.org/uniprotkb/Q8IV50) · Ensembl [ENSG00000140280](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140280)

## Data

Gene col 6384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6384); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6384]; `tensor/DDL_lfc|DDL_z.npy` [6384]; `embed/gene_vectors.npy` [6384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6384 or target_col == 6384). Every well: [[LYSMD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYSMD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
