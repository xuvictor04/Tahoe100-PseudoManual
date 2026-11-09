---
symbol: "SEC23A"
type: "gene"
col: 2046
ensembl_id: "ENSG00000100934"
name: "SEC23 homolog A, COPII component"
location: "14q21.1"
module: 56
arm: "+"
pooled_cpm: 193.13
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 34
n_dd_up_clean: 1
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SEC23A

*SEC23 homolog A, COPII component* — 14q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Pravastatin (sodium) (drug)]] 5 µM: 1.24× (z +3.9, q 0.051, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.343× (z -27.2, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPA]] (+0.86, fdr 7e-06), [[COG6]] (+0.86, fdr 7e-06), [[TMEM39A]] (+0.84, fdr 7e-06); moves opposite to [[TSC22D1]] (-0.71, fdr 1e-05), [[CMTR2]] (-0.69, fdr 7e-06), [[PNRC2]] (-0.66, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2046.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.051 | 34/48 (HOP62, NCI-H23, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2046.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.343×** | -27.2 | 0e+00 | 46/48 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.349×** | -20.1 | 0e+00 | 47/48 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.373×** | -18.8 | 0e+00 | 46/48 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.376×** | -18.6 | 0e+00 | 46/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.500×** | -17.8 | 0e+00 | 46/49 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.402×** | -17.3 | 0e+00 | 47/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.417×** | -16.0 | 0e+00 | 45/48 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.534×** | -11.9 | 5e-31 | 41/48 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.541×** | -11.2 | 2e-27 | 45/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.558×** | -11.1 | 8e-27 | 43/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.573×** | -10.2 | 1e-22 | 39/48 (SW 900, H4, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.692×** | -9.6 | 5e-20 | 44/48 (HS-578T, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.626×** | -8.9 | 2e-17 | 43/48 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.660×** | -7.6 | 1e-12 | 41/48 (NCI-H2347, SNU-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.682×** | -7.0 | 1e-10 | 36/50 (LS 180, SW 900, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.695×** | -6.9 | 2e-10 | 38/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.711×** | -6.5 | 3e-09 | 38/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 447 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -35.1) |
| [[HOP62 (line)]] | alt | 296 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -25.2) |
| [[H4 (line)]] | wt | 295 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -21.0) |
| [[hTERT-HPNE (line)]] | wt | 259 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -16.5) |
| [[SW 900 (line)]] | alt | 415 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 193 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -22.7) |
| [[HS-578T (line)]] | alt | 228 | 0 | 12 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -24.8) |
| [[LS 180 (line)]] | wt | 228 | 0 | 12 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -21.6) |
| [[RPMI-7951 (line)]] | alt | 243 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -25.6) |
| [[A498 (line)]] | wt | 196 | 0 | 11 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -22.2) |
| [[CFPAC-1 (line)]] | alt | 308 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -25.5) |
| [[A549 (line)]] | wt | 238 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -19.5) |
| [[Hs 766T (line)]] | wt | 217 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -18.8) |
| [[HT-29 (line)]] | alt | 110 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -24.1) |
| [[J82 (line)]] | alt | 182 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -32.5) |
| [[A-172 (line)]] | wt | 143 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -20.2) |
| [[LoVo (line)]] | wt | 155 | 0 | 9 | — | [[Panobinostat (drug)]] 5 µM 0.286× (z -15.6) |
| [[KATO III (line)]] | alt | 130 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -21.8) |
| [[NCI-H1792 (line)]] | alt | 301 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -19.6) |
| [[HepG2_C3A (line)]] | wt | 169 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 110 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 221 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 178 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 135 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -15.9) |
| [[SNU-423 (line)]] | alt | 155 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -22.7) |
| [[SW1417 (line)]] | alt | 146 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -19.1) |
| [[BT-474 (line)]] | alt | 224 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -19.2) |
| [[NCI-H1573 (line)]] | alt | 176 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 159 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.5) |
| [[C32 (line)]] | wt | 117 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.2) |
| [[PANC-1 (line)]] | alt | 106 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -17.1) |
| [[SW48 (line)]] | wt | 273 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -12.2) |
| [[COLO 205 (line)]] | alt | 130 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.6) |
| [[HCT15 (line)]] | alt | 209 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 236 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.8) |
| [[SW480 (line)]] | alt | 100 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.383× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 174 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -10.2) |
| [[RKO (line)]] | wt | 129 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -8.7) |
| [[SHP-77 (line)]] | alt | 159 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.474× (z -9.1) |
| [[SNU-1 (line)]] | wt | 221 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -14.9) |
| [[SW 1088 (line)]] | alt | 295 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.119× (z -11.2) |
| [[A-427 (line)]] | wt | 149 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.507× (z -9.0) |
| [[AN3 CA (line)]] | alt | 144 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.2) |
| [[SW 1271 (line)]] | alt | 218 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -11.7) |
| [[C-33 A (line)]] | alt | 156 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPA]] | +0.86 | +0.88 / +0.84 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 688 |
| [[COG6]] | +0.86 | +0.86 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[TMEM39A]] | +0.84 | +0.86 / +0.81 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.84 | +0.89 / +0.69 | both halves | 7e-06 | STRING 796 |
| [[SEC24D]] | +0.83 | +0.85 / +0.77 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[COPB1]] | +0.81 | +0.83 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 607 |
| [[PDXDC2P]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[SEC63]] | +0.79 | +0.77 / +0.71 | both halves | 7e-06 | STRING 457 |
| [[GFPT1]] | +0.79 | +0.83 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDXDC1]] | +0.79 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[SEC13]] | +0.78 | +0.82 / +0.69 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[SEC31A]] | +0.77 | +0.77 / +0.76 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D1]] | -0.71 | -0.73 / -0.53 | both halves | 1e-05 |  |
| [[CMTR2]] | -0.69 | -0.71 / -0.66 | both halves | 7e-06 |  |
| [[PNRC2]] | -0.66 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[ZNF629]] | -0.64 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[TET3]] | -0.63 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SEC23A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MCTP2]] | B | MCTP2 activity raises SEC23A's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.21× lower at baseline in the lines without MCTP2 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, -32.8); signed map (-51.1, 9.9). **Vector** length 112, 45.9% of its response variance represented; |z| ≥ 3 in 1,469 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *protein secretion* (hallmark, mean cos +0.65 to 10); *COPI-dependent Golgi-to-ER retrograde traffic* (reactome, mean cos +0.69 to 9); *COPI-mediated anterograde transport* (reactome, mean cos +0.71 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +11.5 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +11.1 | -1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +7.8 | -6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.2 | -20.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | -18.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | -5.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.6 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | -3.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.2 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.0 | -8.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -16.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -5.3 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.6 | -4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -9.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.7 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | SEC23 homolog A, COPII component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.1 — chr14:39,031,919-39,109,646 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Coat protein complex II |
| Reactome | 19 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; Cargo concentration in the ER; Regulation of cholesterol biosynthesis by SREBP (SREBF) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15436](https://www.uniprot.org/uniprotkb/Q15436) (Protein transport protein Sec23A):

> Component of the coat protein complex II (COPII) which promotes the formation of transport vesicles from the endoplasmic reticulum (ER). The coat has two main functions, the physical deformation of the endoplasmic reticulum membrane into vesicles and the selection of cargo molecules for their transport to the Golgi complex. Required for the translocation of insulin-induced glucose transporter SLC2A4/GLUT4 to the cell membrane (By similarity).

**Summary**, from NCBI Gene [10484](https://www.ncbi.nlm.nih.gov/gene/10484):

> The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is suggested to play a role in the ER-Golgi protein trafficking. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10701) · Entrez [10484](https://www.ncbi.nlm.nih.gov/gene/10484) · UniProt [Q15436](https://www.uniprot.org/uniprotkb/Q15436) · Ensembl [ENSG00000100934](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100934)

## Data

Gene col 2046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2046); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2046]; `tensor/DDL_lfc|DDL_z.npy` [2046]; `embed/gene_vectors.npy` [2046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2046 or target_col == 2046). Every well: [[SEC23A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC23A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
