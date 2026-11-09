---
symbol: "G3BP2"
type: "gene"
col: 6226
ensembl_id: "ENSG00000138757"
name: "G3BP stress granule assembly factor 2"
location: "4q21.1"
module: 42
arm: "+"
pooled_cpm: 176.08
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# G3BP2

*G3BP stress granule assembly factor 2* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.74× (z +11.5, q 6e-28, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.79× (z +11.2, q 2e-26, up in 46 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.409×, KATO III 0.470×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.611×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.537×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA3]] (+0.67, fdr 7e-06), [[MLEC]] (+0.64, fdr 1e-05), [[PDIA6]] (+0.63, fdr 1e-05); moves opposite to [[TATDN1]] (-0.62, fdr 7e-06), [[TRMT61A]] (-0.55, fdr 1e-05), [[MRPL58]] (-0.54, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.74×** | +11.5 | 6e-28 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.79×** | +11.2 | 2e-26 | 46/49 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +9.4 | 9e-19 | 36/49 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.54×** | +9.0 | 3e-17 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.44×** | +7.6 | 4e-12 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.43×** | +7.4 | 1e-11 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +6.8 | 7e-10 | 37/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +5.3 | 1e-05 | 29/48 (BT-474, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.27×** | +4.9 | 7e-05 | 34/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.27×** | +4.6 | 2e-04 | 23/45 (PANC-1, A-172, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.26×** | +4.6 | 2e-04 | 26/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.25×** | +4.6 | 2e-04 | 28/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.24×** | +4.5 | 3e-04 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.24×** | +4.4 | 4e-04 | 30/48 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.19× | +3.5 | 0.016 | 22/50 (A-427, HEC-1-A, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.017 | 19/48 (HOP62, HT-29, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6226.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.409×, KATO III 0.470×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.611×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.537×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | 0.837× | -3.6 | 0.21 | 22/48 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.898× | -3.1 | 0.25 | 2/49 (SNU-1, NCI-H1792) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.864× | -3.0 | 0.25 | 15/48 (NCI-H2347, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 131 | 6 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.66× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 152 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +13.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 178 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +14.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.78× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 148 | 4 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.54× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 250 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.32× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 180 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.74× (z +10.4) | — |
| [[LoVo (line)]] | wt | 197 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +13.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 177 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +10.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 378 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.78× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C32 (line)]] | wt | 202 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.06× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 145 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 170 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 164 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 136 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +9.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 89.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +8.8) | — |
| [[A-427 (line)]] | wt | 219 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.611× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 161 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 215 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +9.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 147 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.470× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 103 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 154 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 141 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 172 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2347 (line)]] | alt | 280 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.537× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 184 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 274 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.67× (z +10.8) | — |
| [[A498 (line)]] | wt | 223 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 226 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 205 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 187 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 150 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 161 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 183 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA3]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[MLEC]] | +0.64 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[PDIA6]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[HSP90B1]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ADAM10]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ALKBH5]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[CNOT6L]] | +0.58 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[TMED4]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[P3H1]] | +0.56 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[GLG1]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SBNO1]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SLC39A7]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TATDN1]] | -0.62 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[TRMT61A]] | -0.55 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[MRPL58]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ITPA]] | -0.53 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[TRMT10B]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[HUS1]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ZC3HC1]] | -0.51 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[GLRX2]] | -0.50 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[SLC9A8]] | -0.50 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[YTHDC2]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 | STRING 507 |
| [[PLEKHG4]] | -0.49 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[NT5C]] | -0.49 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.6, -29.4); signed map (-55.0, 5.9). **Vector** length 103, 32.1% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.1 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -9.1 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.0 | -0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | +0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.2 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.1 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | G3BP stress granule assembly factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:75,641,849-75,724,589 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0660 |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 5 pathways, smallest: SARS-CoV-2 activates/modulates innate and adaptive immune responses; SARS-CoV-2-host interactions; SARS-CoV-2 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UN86](https://www.uniprot.org/uniprotkb/Q9UN86) (Ras GTPase-activating protein-binding protein 2):

> Scaffold protein that plays an essential role in cytoplasmic stress granule formation which acts as a platform for antiviral signaling. Plays an essential role in stress granule formation. Stress granules are membraneless compartments that store mRNAs and proteins, such as stalled translation pre-initiation complexes, in response to stress. Promotes formation of stress granules phase-separated membraneless compartment by undergoing liquid-liquid phase separation (LLPS) upon unfolded …

**Summary**, from NCBI Gene [9908](https://www.ncbi.nlm.nih.gov/gene/9908):

> Enables molecular condensate scaffold activity. Involved in protein homooligomerization and stress granule assembly. Located in cytoplasmic stress granule and cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30291) · Entrez [9908](https://www.ncbi.nlm.nih.gov/gene/9908) · UniProt [Q9UN86](https://www.uniprot.org/uniprotkb/Q9UN86) · Ensembl [ENSG00000138757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138757)

## Data

Gene col 6226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6226); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6226]; `tensor/DDL_lfc|DDL_z.npy` [6226]; `embed/gene_vectors.npy` [6226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6226 or target_col == 6226). Every well: [[G3BP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/G3BP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
