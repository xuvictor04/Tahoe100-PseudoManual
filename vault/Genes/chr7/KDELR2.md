---
symbol: "KDELR2"
type: "gene"
col: 5840
ensembl_id: "ENSG00000136240"
name: "KDEL endoplasmic reticulum protein retention receptor 2"
location: "7p22.1"
module: 56
arm: "+"
pooled_cpm: 235.73
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 32
n_dd_up_clean: 1
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# KDELR2

*KDEL endoplasmic reticulum protein retention receptor 2* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.45× (z +6.7, q 1e-08, up in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 2.55×, SNU-423 2.29×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SW1417 1.83×, SNU-423 2.04×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 2.23×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.443× (z -20.8, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDXDC1]] (+0.88, fdr 7e-06), [[SEC31A]] (+0.86, fdr 7e-06), [[SEC24D]] (+0.86, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FBXO16]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5840.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 2.55×, SNU-423 2.29×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SW1417 1.83×, SNU-423 2.04×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 2.23×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +6.7 | 1e-08 | 36/48 (SW1417, SNU-423, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.14× | +3.4 | 0.21 | 7/49 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.31 | 5/49 (BT-474, RKO, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.31 | 22/48 (SW480, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.443×** | -20.8 | 0e+00 | 46/48 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.432×** | -14.6 | 1e-45 | 48/48 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.544×** | -11.0 | 7e-26 | 40/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.588×** | -9.6 | 2e-19 | 43/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.691×** | -9.4 | 6e-19 | 43/48 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.701×** | -9.1 | 1e-17 | 43/48 (A-427, SW 900, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -8.9 | 6e-17 | 37/49 (SW 900, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.624×** | -8.5 | 1e-15 | 38/48 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.650×** | -7.8 | 5e-13 | 39/48 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.665×** | -7.4 | 1e-11 | 35/48 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.664×** | -6.6 | 2e-09 | 42/48 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.694×** | -6.6 | 2e-09 | 32/48 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.685×** | -6.6 | 2e-09 | 38/48 (LoVo, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -6.3 | 2e-08 | 35/48 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.716×** | -5.8 | 3e-07 | 36/48 (SW 900, hTERT-HPNE, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.734×** | -5.2 | 5e-06 | 36/47 (Panc 03.27, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.748×** | -4.8 | 4e-05 | 29/47 (A-172, H4, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 764 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -23.6) |
| [[hTERT-HPNE (line)]] | wt | 298 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -18.3) |
| [[SW 900 (line)]] | alt | 260 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -19.7) |
| [[HOP62 (line)]] | alt | 288 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -27.5) |
| [[HS-578T (line)]] | alt | 341 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -31.0) |
| [[A-172 (line)]] | wt | 325 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -22.4) |
| [[A498 (line)]] | wt | 443 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -20.4) |
| [[RPMI-7951 (line)]] | alt | 344 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -22.9) |
| [[A549 (line)]] | wt | 180 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -16.5) |
| [[LoVo (line)]] | wt | 301 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.296× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 347 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -15.3) |
| [[SNU-423 (line)]] | alt | 177 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.04× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.2) |
| [[A-427 (line)]] | wt | 110 | 1 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 2.23× (z +9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -14.1) |
| [[HT-29 (line)]] | alt | 285 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -19.0) |
| [[J82 (line)]] | alt | 227 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 134 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.333× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 210 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -19.4) |
| [[SW 1088 (line)]] | alt | 516 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -16.4) |
| [[SW1417 (line)]] | alt | 219 | 1 | 3 | [[Auranofin (drug)]] 5 µM 1.83× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -21.9) |
| [[AsPC-1 (line)]] | alt | 356 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -13.6) |
| [[Hs 766T (line)]] | wt | 317 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -20.3) |
| [[KATO III (line)]] | alt | 328 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -14.9) |
| [[LS 180 (line)]] | wt | 206 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 205 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -21.5) |
| [[SNU-1 (line)]] | wt | 193 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.246× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 192 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 189 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -14.5) |
| [[PANC-1 (line)]] | alt | 228 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -11.3) |
| [[SHP-77 (line)]] | alt | 118 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -11.8) |
| [[SW480 (line)]] | alt | 195 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.368× (z -10.4) |
| [[BT-474 (line)]] | alt | 273 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -13.7) |
| [[CFPAC-1 (line)]] | alt | 147 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 222 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 167 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.377× (z -8.5) |
| [[RKO (line)]] | wt | 163 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -12.5) |
| [[SW48 (line)]] | wt | 266 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -10.2) |
| [[AN3 CA (line)]] | alt | 147 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 121 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 95.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 239 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDXDC1]] | +0.88 | +0.89 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[SEC31A]] | +0.86 | +0.87 / +0.81 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC24D]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 496 |
| [[SEC13]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 409 |
| [[PGM3]] | +0.84 | +0.85 / +0.85 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[COG6]] | +0.82 | +0.86 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[HM13]] | +0.81 | +0.81 / +0.79 | both halves | 7e-06 |  |
| [[KDELR3]] | +0.81 | +0.82 / +0.76 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 922 |
| [[COG3]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDXDC2P]] | +0.80 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[TMED3]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 612 |
| [[SEC22B]] | +0.79 | +0.81 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 651 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO16]] | B | FBXO16 activity lowers KDELR2's level | lines that do not express FBXO16 (9) vs lines expressing it (41) | 1.41× higher at baseline in the lines without FBXO16 | 0.044 | ⚠ within organs, on part of the lines; also absent: FZD3, PTPRU, OTUD7A; maybe low, not absent |
| [[SLC1A1]] | B | SLC1A1 activity strengthens KDELR2's drug response | lines that do not express SLC1A1 (11) vs lines expressing it (38) | the lines without SLC1A1 respond 0.66× as strongly (z diff +2.11); strongest at Panobinostat 5 µM: 0.84x vs 0.58x (z diff +3.9) | 0.058 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SLC1A1]] | B | SLC1A1 activity raises KDELR2's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without SLC1A1 | 0.070 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[SNHG18]] | B | SNHG18 activity raises KDELR2's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.56× lower at baseline in the lines without SNHG18 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[SEC13]] | C | SEC13's natural level strengthens KDELR2's drug response | SEC13's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.40; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | KDELR2's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | KDELR2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61 | 0.452 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.909). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.0, -33.8); signed map (-51.2, 10.6). **Vector** length 150, 61.4% of its response variance represented; |z| ≥ 3 in 1,436 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *protein secretion* (hallmark, mean cos +0.68 to 10); *COPII-mediated vesicle transport* (reactome, mean cos +0.73 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.72 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.4 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.3 | -8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | -7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.0 | +1.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.3 | +2.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +3.2 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.9 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.7 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.7 | -9.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.3 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.0 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | KDEL endoplasmic reticulum protein retention receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,445,953-6,484,190 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ELP-1, ERD2.2 |
| Gene groups (HGNC) | KDEL endoplasmic reticulum protein retention receptors |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P33947](https://www.uniprot.org/uniprotkb/P33947) (ER lumen protein-retaining receptor 2):

> Membrane receptor that binds the K-D-E-L sequence motif in the C-terminal part of endoplasmic reticulum resident proteins and maintains their localization in that compartment by participating to their vesicle-mediated recycling back from the Golgi. Binding is pH dependent, and is optimal at pH 5-5.4 (By similarity).

**Summary**, from NCBI Gene [11014](https://www.ncbi.nlm.nih.gov/gene/11014):

> Retention of resident soluble proteins in the lumen of the endoplasmic reticulum (ER) is achieved in both yeast and animal cells by their continual retrieval from the cis-Golgi, or a pre-Golgi compartment. Sorting of these proteins is dependent on a C-terminal tetrapeptide signal, usually lys-asp-glu-leu (KDEL) in animal cells, and his-asp-glu-leu (HDEL) in S. cerevisiae. This process is mediated by a receptor that recognizes, and binds the tetrapeptide-containing protein, and returns it to the …

**Accessions** — [HGNC:6305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6305) · Entrez [11014](https://www.ncbi.nlm.nih.gov/gene/11014) · UniProt [P33947](https://www.uniprot.org/uniprotkb/P33947) · Ensembl [ENSG00000136240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136240)

## Data

Gene col 5840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5840); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5840]; `tensor/DDL_lfc|DDL_z.npy` [5840]; `embed/gene_vectors.npy` [5840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5840 or target_col == 5840). Every well: [[KDELR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDELR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
