---
symbol: "DYNC1LI2"
type: "gene"
col: 5745
ensembl_id: "ENSG00000135720"
name: "dynein cytoplasmic 1 light intermediate chain 2"
location: "16q22.1"
module: 42
arm: "+"
pooled_cpm: 153.28
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# DYNC1LI2

*dynein cytoplasmic 1 light intermediate chain 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.52× (z +11.9, q 1e-29, up in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.33× (z +8.1, q 8e-14, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.826× (z -7.8, q 5e-12, down in 21 of 49 measured lines) ⚠ cell-cycle shift, explains ~8% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (HS-578T 0.625×, HOP62 0.681×, A498 0.708×, RPMI-7951 0.643×; ⚠ cell-cycle shift, explains ~8% of this change); [[Capmatinib (drug)]] 5 µM in 1 line (CHP-212 0.0823×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAM2]] (+0.68, fdr 7e-06), [[HDLBP]] (+0.63, fdr 1e-05), [[RTF2]] (+0.63, fdr 7e-06); moves opposite to [[ZNF670]] (-0.63, fdr 1e-05), [[ZNRF2P1]] (-0.53, fdr 3e-05), [[ENDOG]] (-0.52, fdr 9e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +11.9 | 1e-29 | 40/49 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +10.8 | 1e-24 | 33/44 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +10.0 | 2e-21 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +8.1 | 8e-14 | 34/48 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +7.2 | 6e-11 | 33/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +6.1 | 8e-08 | 25/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +6.1 | 8e-08 | 26/48 (A-427, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.15× | +5.7 | 1e-06 | 18/48 (C32, NCI-H1792, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.23×** | +5.5 | 2e-06 | 27/48 (PANC-1, C32, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +4.8 | 1e-04 | 20/48 (PANC-1, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 2e-04 | 22/45 (A-427, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.4 | 0.035 | 21/45 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.08× | +3.1 | 0.084 | 3/49 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.12× | +3.1 | 0.084 | 8/48 (A498, NCI-H2030, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.11× | +3.1 | 0.084 | 7/48 (HT-29, COLO 205, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5745.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (HS-578T 0.625×, HOP62 0.681×, A498 0.708×, RPMI-7951 0.643×; ⚠ cell-cycle shift, explains ~8% of this change); [[Capmatinib (drug)]] 5 µM in 1 line (CHP-212 0.0823×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.826×** | -7.8 | 5e-12 | 21/49 (HS-578T, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.877× | -3.8 | 0.049 | 13/48 (CFPAC-1, H4, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.879× | -3.5 | 0.088 | 12/47 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.888× | -3.4 | 0.091 | 11/48 (HOP62, H4, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.893× | -3.3 | 0.12 | 12/48 (RKO, hTERT-HPNE, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.856× | -3.2 | 0.13 | 16/48 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 108 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.33× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +10.0) | — |
| [[A-427 (line)]] | wt | 133 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.33× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.72× (z +8.8) | — |
| [[C32 (line)]] | wt | 105 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +13.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 138 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 131 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 161 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.92× (z +11.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 170 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 182 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 172 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.4) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +14.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 188 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.60× (z +9.3) | — |
| [[A549 (line)]] | wt | 145 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.72× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 209 | 0 | 1 | — | [[Capmatinib (drug)]] 5 µM 0.0823× (z -11.4) |
| [[Hs 766T (line)]] | wt | 157 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -10.8) ⚠ cell-cycle shift, explains ~8% of this change |
| [[HT-29 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +8.6) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[Panc 03.27 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.91× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -8.5) ⚠ cell-cycle shift, explains ~8% of this change |
| [[SHP-77 (line)]] | alt | 95.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 143 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 146 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 143 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 138 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 175 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 123 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 132 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 204 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 127 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 139 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAM2]] | +0.68 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[HDLBP]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[RTF2]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[EIF2AK1]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[VAMP7]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[USO1]] | +0.57 | +0.45 / +0.63 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[BMS1P20]] | +0.56 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ZBTB41]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SUDS3]] | +0.55 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[SYNJ2BP]] | +0.55 | +0.31 / +0.63 | both halves | 2e-04 |  |
| [[SPTAN1]] | +0.55 | +0.40 / +0.56 | both halves | 4e-05 | pathway: Asparagine N-linked glycosylation |
| [[DYNC1I2]] | +0.55 | +0.58 / +0.46 | both halves | 3e-05 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 999 |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF670]] | -0.63 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[ZNRF2P1]] | -0.53 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ENDOG]] | -0.52 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[C9orf40]] | -0.50 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SUZ12P1]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[TIMM10]] | -0.50 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[MIR17HG]] | -0.49 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[LRCH1]] | -0.49 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[UCK2]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[OXLD1]] | -0.48 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[SNRPB]] | -0.48 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[F12]] | -0.48 | -0.16 / -0.67 | ⚠ one half (not replicated) | 0.001 |  |
| [[PTGR3]] | -0.47 | -0.46 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers DYNC1LI2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.386). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.8, -17.2); signed map (-31.4, -24.7). **Vector** length 114, 30.2% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +11.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.9 | +2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.5 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -7.7 | -7.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.8 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | +0.1 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | -2.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | dynein cytoplasmic 1 light intermediate chain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:66,720,893-66,751,609 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DNCLI2 |
| Gene groups (HGNC) | Dynein 1 complex subunits; Dynein light intermediate chains |
| Reactome | 41 pathways, smallest: Aggrephagy; COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [O43237](https://www.uniprot.org/uniprotkb/O43237) (Cytoplasmic dynein 1 light intermediate chain 2):

> Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 1 complex that are thought to be involved in linking dynein to cargos and to adapter proteins that regulate dynein function. Cytoplasmic dynein 1 acts as a motor for the intracellular retrograde motility of vesicles and organelles along microtubules. May play a role in binding dynein to membranous organelles or chromosomes.

**Summary**, from NCBI Gene [1783](https://www.ncbi.nlm.nih.gov/gene/1783):

> Cytoplasmic dynein is a microtubule-associated motor protein (Hughes et al., 1995 [PubMed 7738094]). See DYNC1H1 (MIM 600112) for general information about dyneins.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:2966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2966) · Entrez [1783](https://www.ncbi.nlm.nih.gov/gene/1783) · UniProt [O43237](https://www.uniprot.org/uniprotkb/O43237) · Ensembl [ENSG00000135720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135720)

## Data

Gene col 5745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5745); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5745]; `tensor/DDL_lfc|DDL_z.npy` [5745]; `embed/gene_vectors.npy` [5745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5745 or target_col == 5745). Every well: [[DYNC1LI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNC1LI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
