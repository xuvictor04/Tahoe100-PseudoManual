---
symbol: "PDXDC1"
type: "gene"
col: 11061
ensembl_id: "ENSG00000179889"
name: "pyridoxal dependent decarboxylase domain containing 1"
location: "16p13.11"
module: 56
arm: "+"
pooled_cpm: 179.94
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 38
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# PDXDC1

*pyridoxal dependent decarboxylase domain containing 1* — 16p13.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.538× (z -17.5, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDXDC2P]] (+0.96, fdr 7e-06), [[PDXDC2P-NPIPB14P]] (+0.91, fdr 7e-06), [[KDELR2]] (+0.88, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC1A1]] → it (grade B ⚠); 2 go from it, the strongest it → [[PMM2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-733 (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.95 | 16/48 (LoVo, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 26 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11061.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.538×** | -17.5 | 0e+00 | 41/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.452×** | -15.4 | 0e+00 | 43/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.499×** | -14.0 | 3e-42 | 44/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -12.0 | 4e-31 | 40/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.562×** | -11.6 | 4e-29 | 44/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.708×** | -9.7 | 3e-20 | 36/48 (HS-578T, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.719×** | -9.3 | 1e-18 | 42/48 (HS-578T, Hs 766T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.630×** | -8.9 | 3e-17 | 37/47 (RKO, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.728×** | -8.9 | 3e-17 | 27/49 (HS-578T, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.664×** | -8.2 | 1e-14 | 29/48 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.678×** | -7.8 | 3e-13 | 32/48 (HS-578T, H4, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.669×** | -7.8 | 4e-13 | 37/48 (LoVo, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.680×** | -7.8 | 4e-13 | 32/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.685×** | -7.6 | 1e-12 | 33/48 (HS-578T, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.691×** | -7.4 | 4e-12 | 37/48 (HT-29, HOP62, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -7.0 | 9e-11 | 33/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.788×** | -6.7 | 6e-10 | 29/48 (HT-29, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.720×** | -6.6 | 1e-09 | 31/48 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.738×** | -5.6 | 4e-07 | 38/47 (A-172, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.784×** | -4.6 | 9e-05 | 27/47 (NCI-H1573, RPMI-7951, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.855× | -4.4 | 2e-04 | 21/48 (A-172, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 235 | 0 | 19 (12 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.172× (z -16.8) |
| [[HS-578T (line)]] | alt | 225 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -25.8) |
| [[hTERT-HPNE (line)]] | wt | 254 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -21.7) |
| [[HOP62 (line)]] | alt | 201 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -22.5) |
| [[A-172 (line)]] | wt | 205 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -24.2) |
| [[AsPC-1 (line)]] | alt | 447 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -27.4) |
| [[Hs 766T (line)]] | wt | 208 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 175 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -20.8) |
| [[A498 (line)]] | wt | 348 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -21.7) |
| [[KATO III (line)]] | alt | 330 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -14.3) |
| [[SW 900 (line)]] | alt | 207 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -17.0) |
| [[HT-29 (line)]] | alt | 283 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -18.7) |
| [[COLO 205 (line)]] | alt | 333 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 137 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -17.8) |
| [[A549 (line)]] | wt | 154 | 0 | 5 | — | [[Harringtonine (drug)]] 0.5 µM 0.354× (z -11.4) |
| [[J82 (line)]] | alt | 184 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -19.5) |
| [[SW1417 (line)]] | alt | 251 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -13.6) |
| [[LoVo (line)]] | wt | 287 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.283× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 217 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.424× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 127 | 0 | 4 | — | [[Harringtonine (drug)]] 0.5 µM 0.244× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 159 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 147 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 152 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.6) |
| [[RKO (line)]] | wt | 124 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.256× (z -15.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.527× (z -10.7) |
| [[SNU-1 (line)]] | wt | 139 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.379× (z -8.9) |
| [[A-427 (line)]] | wt | 96.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -12.6) |
| [[BT-474 (line)]] | alt | 165 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 116 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.496× (z -11.2) |
| [[SNU-423 (line)]] | alt | 93.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 69.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.8) |
| [[SW 1088 (line)]] | alt | 351 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -8.7) |
| [[SW 1271 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 363 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 166 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 139 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 89.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 169 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDXDC2P]] | +0.96 | +0.95 / +0.95 | both halves | 7e-06 | **novel candidate** |
| [[PDXDC2P-NPIPB14P]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[KDELR2]] | +0.88 | +0.89 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[SEC31A]] | +0.84 | +0.84 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[COG6]] | +0.83 | +0.87 / +0.75 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.82 | +0.82 / +0.82 | both halves | 7e-06 |  |
| [[SEC13]] | +0.81 | +0.82 / +0.78 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.81 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[COPA]] | +0.79 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.79 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[COPB1]] | +0.77 | +0.83 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC1A1]] | B | SLC1A1 activity raises PDXDC1's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.69× lower at baseline in the lines without SLC1A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[MCTP2]] | B | MCTP2 activity raises PDXDC1's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.56× lower at baseline in the lines without MCTP2 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[TOP2A]] | B | TOP2A activity raises PDXDC1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TBC1D8B]] | B | TBC1D8B activity raises PDXDC1's level | lines that do not express TBC1D8B (6) vs lines expressing it (44) | 1.60× lower at baseline in the lines without TBC1D8B | 0.089 | ⚠ within organs, on part of the lines; also absent: AHR, MYO1B, RND3; its own permutation p |
| [[MCTP2]] | B | MCTP2 activity strengthens PDXDC1's drug response | lines that do not express MCTP2 (20) vs lines expressing it (29) | the lines without MCTP2 respond 0.61× as strongly (z diff +2.43); strongest at Idarubicin (hydrochloride) 5 µM: 0.91x vs 0.65x (z diff +4.2) | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMM2]] | C | PDXDC1's natural level strengthens PMM2's drug response | PDXDC1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.33; direction not clear | 0.040 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ARF4]] | C | PDXDC1's natural level strengthens ARF4's drug response | PDXDC1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.43; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.901). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, -33.9); signed map (-50.4, 10.6). **Vector** length 140, 54.5% of its response variance represented; |z| ≥ 3 in 1,492 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.71 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.72 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.72 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +6.1 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.6 | -7.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.0 | -7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.9 | -3.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.7 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -9.3 | -11.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.1 | -14.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.6 | -9.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.4 | -7.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.8 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -9.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | pyridoxal dependent decarboxylase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:14,974,591-15,139,339 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0251 |
| Matched by | ensembl_id |

UniProt [Q6P996](https://www.uniprot.org/uniprotkb/Q6P996) carries no function annotation.

**Summary**, from NCBI Gene [23042](https://www.ncbi.nlm.nih.gov/gene/23042):

> Enables cadherin binding activity. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28995) · Entrez [23042](https://www.ncbi.nlm.nih.gov/gene/23042) · UniProt [Q6P996](https://www.uniprot.org/uniprotkb/Q6P996) · Ensembl [ENSG00000179889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179889)

## Data

Gene col 11061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11061); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11061]; `tensor/DDL_lfc|DDL_z.npy` [11061]; `embed/gene_vectors.npy` [11061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11061 or target_col == 11061). Every well: [[PDXDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDXDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
