---
symbol: "PEX2"
type: "gene"
col: 9002
ensembl_id: "ENSG00000164751"
name: "peroxisomal biogenesis factor 2"
location: "8q21.13"
module: 220
arm: "+"
pooled_cpm: 26.13
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/220"]
generated_by: "tahoemap"
---

# PEX2

*peroxisomal biogenesis factor 2* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 1.20× (z +5.3, q 5e-05, up in 20 of 48 measured lines) ⚠ cell-cycle shift, explains ~13% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.55× (z +4.7, q 6e-04, up in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 2.24×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.643× (z -12.9, q 2e-35, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFV2]] (+0.66, fdr 7e-06), [[MRPS31P5-1]] (+0.65, fdr 1e-05), [[UBXN2B]] (+0.64, fdr 1e-05); moves opposite to [[PPIEL-1]] (-0.65, fdr 1e-05), [[QRICH2]] (-0.63, fdr 7e-06), [[ZDHHC11]] (-0.62, fdr 1e-05).
> It is in [[Module 220]], a single-armed module (Respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9002.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 2.24×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.20× | +5.3 | 5e-05 | 20/48 (LS 180, A-172, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +4.7 | 6e-04 | 15/48 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.50×** | +4.4 | 0.002 | 18/46 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.15× | +4.2 | 0.004 | 9/48 (SW480, HepG2/C3A, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.21 | 4/48 (HOP62, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9002.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -12.9 | 2e-35 | 37/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.707×** | -10.1 | 1e-21 | 32/47 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -6.7 | 4e-09 | 27/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.803×** | -6.4 | 2e-08 | 26/48 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.720×** | -6.3 | 4e-08 | 21/37 (KATO III, LS 180, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -6.2 | 5e-08 | 25/47 (C-33 A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.751×** | -5.9 | 3e-07 | 21/48 (RKO, Hs 766T, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.768×** | -5.2 | 1e-05 | 20/48 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.774×** | -5.1 | 2e-05 | 22/47 (CHP-212, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.793×** | -4.8 | 1e-04 | 18/47 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.798×** | -4.6 | 2e-04 | 20/48 (SW480, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.813×** | -4.3 | 9e-04 | 17/48 (NCI-H1573, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.720×** | -3.5 | 0.017 | 16/41 (SNU-423, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.843× | -3.5 | 0.018 | 10/47 (SNU-1, H4, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.729×** | -3.4 | 0.024 | 11/46 (NCI-H1573, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.731×** | -3.4 | 0.025 | 10/46 (NCI-H2347, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.844× | -3.4 | 0.025 | 13/48 (NCI-H2030, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 31.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0927× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -11.3) |
| [[A549 (line)]] | wt | 21.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 14.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.4) |
| [[RKO (line)]] | wt | 36.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.317× (z -8.7) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 27.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -15.7) |
| [[A498 (line)]] | wt | 35.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -8.6) |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -9.1) |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -10.5) ⚠ toxic |
| [[C32 (line)]] | wt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[CHP-212 (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.114× (z -8.5) ⚠ transcription drop |
| [[LS 180 (line)]] | wt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 39.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 17.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.0) |
| [[SHP-77 (line)]] | alt | 41.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.1) |
| [[A-172 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFV2]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[MRPS31P5-1]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[UBXN2B]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MRPL22]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[USP30]] | +0.64 | +0.71 / +0.54 | both halves | 1e-05 | STRING 400 |
| [[TRAPPC11]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[METTL14]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[DYNC2LI1]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[COA5]] | +0.63 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[NDUFB6]] | +0.63 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[NDUFS4]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[JKAMP]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIEL-1]] | -0.65 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[QRICH2]] | -0.63 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[ZDHHC11]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[GARIN1A]] | -0.62 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[CSPG5]] | -0.62 | -0.63 / -0.57 | both halves | 8e-06 |  |
| [[CHADL]] | -0.61 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[PPIEL]] | -0.60 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[MELTF]] | -0.59 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[GATAD2A]] | -0.59 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[CEACAM19]] | -0.59 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[SFXN5]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PEX2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 220]] — Respiratory electron transport; 11 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.4, -10.5); signed map (-29.1, -12.7). **Vector** length 81.9, 15.4% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Respiratory electron transport* (reactome, mean cos +0.60 to 4); *Complex I biogenesis* (reactome, mean cos +0.59 to 3); *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.60 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +6.4 | +5.3 |
|  | [[NG25 (drug)]] 5 µM |  | +4.2 | +4.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.0 | +1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.4 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -12.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.4 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.1 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -6.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:76,980,258-77,001,044 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PMP35, PAF-1, RNF72, ZWS3; previously PXMP3 |
| Gene groups (HGNC) | Ring finger proteins; Peroxins; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | PEROXISOME |
| Reactome | 5 pathways, smallest: Class I peroxisomal membrane protein import; E3 ubiquitin ligases ubiquitinate target proteins; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [P28328](https://www.uniprot.org/uniprotkb/P28328) (Peroxisome biogenesis factor 2):

> E3 ubiquitin-protein ligase component of a retrotranslocation channel required for peroxisome organization by mediating export of the PEX5 receptor from peroxisomes to the cytosol, thereby promoting PEX5 recycling. The retrotranslocation channel is composed of PEX2, PEX10 and PEX12; each subunit contributing transmembrane segments that coassemble into an open channel that specifically allows the passage of PEX5 through the peroxisomal membrane (By similarity). PEX2 also regulates peroxisome …

**Summary**, from NCBI Gene [5828](https://www.ncbi.nlm.nih.gov/gene/5828):

> This gene encodes an integral peroxisomal membrane protein required for peroxisome biogenesis. The protein is thought to be involved in peroxisomal matrix protein import. Mutations in this gene result in one form of Zellweger syndrome and infantile Refsum disease. Alternative splicing results in multiple transcript variants encoding the same protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9717) · Entrez [5828](https://www.ncbi.nlm.nih.gov/gene/5828) · UniProt [P28328](https://www.uniprot.org/uniprotkb/P28328) · Ensembl [ENSG00000164751](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164751)

## Data

Gene col 9002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9002); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9002]; `tensor/DDL_lfc|DDL_z.npy` [9002]; `embed/gene_vectors.npy` [9002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9002 or target_col == 9002). Every well: [[PEX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
