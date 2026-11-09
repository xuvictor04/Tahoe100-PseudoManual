---
symbol: "DNAJB9"
type: "gene"
col: 4898
ensembl_id: "ENSG00000128590"
name: "DnaJ heat shock protein family (Hsp40) member B9"
location: "7q31.1"
module: 49
arm: "+"
pooled_cpm: 51.22
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# DNAJB9

*DnaJ heat shock protein family (Hsp40) member B9* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.14× (z +4.1, q 0.023, up in 2 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +3.8, q 0.042, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (NCI-H1573 6.37×, LoVo 4.97×, COLO 205 5.98×; ⚠ cell-cycle shift, explains ~33% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 3.96×); [[Harringtonine (drug)]] 5 µM in 1 line (COLO 205 6.00×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H1792 3.48×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.466× (z -7.3, q 1e-10, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.720× (z -3.9, q 0.006, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERP1]] (+0.74, fdr 7e-06), [[CCDC186]] (+0.72, fdr 1e-05), [[SELENOS]] (+0.70, fdr 7e-06); moves opposite to [[EFTUD2]] (-0.56, fdr 6e-05), [[LMNB2]] (-0.55, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CADPS2]] → it (grade B ⚠); 2 go from it, the strongest it → [[SELENOK]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4898.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (NCI-H1573 6.37×, LoVo 4.97×, COLO 205 5.98×; ⚠ cell-cycle shift, explains ~33% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 3.96×); [[Harringtonine (drug)]] 5 µM in 1 line (COLO 205 6.00×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H1792 3.48×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.1 | 0.023 | 2/49 (SHP-77, CHP-212) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.042 | 27/48 (J82, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4898.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.466×** | -7.3 | 1e-10 | 47/48 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.589×** | -5.1 | 1e-04 | 30/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.608×** | -4.8 | 3e-04 | 26/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.597×** | -4.8 | 3e-04 | 24/38 (KATO III, NCI-H1573, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.625×** | -4.4 | 0.001 | 25/47 (NCI-H1573, COLO 205, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.633×** | -4.1 | 0.005 | 22/42 (RKO, HS-578T, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.720×** | -3.9 | 0.006 | 29/48 (AsPC-1, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.679×** | -3.7 | 0.018 | 27/48 (HT-29, LS 180, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.685×** | -3.6 | 0.018 | 26/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.690×** | -3.5 | 0.026 | 32/48 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.743×** | -3.5 | 0.028 | 26/47 (HS-578T, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.516×** | -3.3 | 0.043 | 25/49 (A-172, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.719×** | -3.2 | 0.066 | 22/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.534×** | -3.1 | 0.066 | 24/48 (SNU-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -3.1 | 0.085 | 22/48 (LS 180, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 70.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.98× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.96× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 90.2 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.37× (z +14.2) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.0865× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[LoVo (line)]] | wt | 73.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.97× (z +12.6) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.283× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[RKO (line)]] | wt | 60.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.339× (z -8.8) |
| [[H4 (line)]] | wt | 64.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0645× (z -14.6) ⚠ toxic; cell-cycle shift, explains ~85% of this change |
| [[HS-578T (line)]] | alt | 89.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -11.8) |
| [[HT-29 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[KATO III (line)]] | alt | 98.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0373× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 53.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -8.8) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 82.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H1792 (line)]] | alt | 57.0 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.48× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.341× (z -9.0) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 27.2 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.168× (z -8.5) |
| [[SW1417 (line)]] | alt | 79.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 70.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERP1]] | +0.74 | +0.80 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 509 |
| [[CCDC186]] | +0.72 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[SELENOS]] | +0.70 | +0.75 / +0.70 | both halves | 7e-06 | STRING 522 |
| [[SELENOK]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[CDK2AP2]] | +0.69 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[IFT20]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[AKAP17A]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[STX5-DT]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[BET1]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.68 | +0.73 / +0.58 | both halves | 7e-06 | same gene group |
| [[GOLGA5]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PGM3]] | +0.67 | +0.72 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | -0.56 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[LMNB2]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADPS2]] | B | CADPS2 activity raises DNAJB9's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without CADPS2 | 0.076 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SELENOK]] | C | DNAJB9's natural level weakens SELENOK's drug response | DNAJB9's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.43; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[DNAJC3]] | C | DNAJB9's natural level weakens DNAJC3's drug response | DNAJB9's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.43; direction not clear | 0.097 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.636). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.6, -38.6); signed map (-49.0, 14.3). **Vector** length 136, 44.0% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.58 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -0.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.7 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.6 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.5 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.3 | +2.2 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.7 | -7.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.9 | -2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.4 | -2.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.9 | -1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member B9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:108,569,867-108,574,850 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MDG1 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Hallmark sets | ANDROGEN_RESPONSE, UNFOLDED_PROTEIN_RESPONSE, ADIPOGENESIS |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBS3](https://www.uniprot.org/uniprotkb/Q9UBS3) (DnaJ homolog subfamily B member 9):

> Co-chaperone for Hsp70 protein HSPA5/BiP that acts as a key repressor of the ERN1/IRE1-mediated unfolded protein response (UPR) (By similarity). J domain-containing co-chaperones stimulate the ATPase activity of Hsp70 proteins and are required for efficient substrate recognition by Hsp70 proteins. In the unstressed endoplasmic reticulum, interacts with the luminal region of ERN1/IRE1 and selectively recruits HSPA5/BiP: HSPA5/BiP disrupts the dimerization of the active ERN1/IRE1 luminal region, …

**Summary**, from NCBI Gene [4189](https://www.ncbi.nlm.nih.gov/gene/4189):

> This gene is a member of the J protein family. J proteins function in many cellular processes by regulating the ATPase activity of 70 kDa heat shock proteins. This gene is a member of the type 2 subgroup of DnaJ proteins. The encoded protein is localized to the endoplasmic reticulum. This protein is induced by endoplasmic reticulum stress and plays a role in protecting stressed cells from apoptosis. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:6968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6968) · Entrez [4189](https://www.ncbi.nlm.nih.gov/gene/4189) · UniProt [Q9UBS3](https://www.uniprot.org/uniprotkb/Q9UBS3) · Ensembl [ENSG00000128590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128590)

## Data

Gene col 4898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4898); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4898]; `tensor/DDL_lfc|DDL_z.npy` [4898]; `embed/gene_vectors.npy` [4898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4898 or target_col == 4898). Every well: [[DNAJB9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJB9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
