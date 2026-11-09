---
symbol: "CACNG6"
type: "gene"
col: 5066
ensembl_id: "ENSG00000130433"
name: "calcium voltage-gated channel auxiliary subunit gamma 6"
location: "19q13.42"
module: 19
arm: "+"
pooled_cpm: 2.72
n_lines_expressing: 32
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CACNG6

*calcium voltage-gated channel auxiliary subunit gamma 6* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 11.0× (z +19.1, q 0e+00, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.70× (z +11.6, q 8e-29, up in 8 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.0299×, NCI-H460 0.117×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.126×, NCI-H2030 0.206×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0970×, A549 0.0866×); [[Panobinostat (drug)]] 5 µM in 2 lines (PANC-1 0.230×, NCI-H460 0.118×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P4HA3]] (+0.63, fdr 1e-05), [[PPEF1]] (+0.61, fdr 4e-05), [[HORMAD1]] (+0.59, fdr 3e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ELOVL2]] → it (grade B ⚠); 4 go from it, the strongest it → [[NOS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **11.0×** | +19.1 | 0e+00 | 5/5 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.09×** | +14.9 | 0e+00 | 7/10 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.21×** | +13.9 | 6e-42 | 5/7 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +11.6 | 8e-29 | 8/16 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +6.3 | 3e-08 | 2/7 (NCI-H2030, CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +4.8 | 1e-04 | 3/12 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.18×** | +4.6 | 4e-04 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.003 | 2/18 (A498, HOP62) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.1 | 0.003 | 3/19 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.005 | 0/26 | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +3.9 | 0.006 | 1/8 (A498) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +3.8 | 0.006 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.6 | 0.013 | 1/15 (CFPAC-1) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.18×** | +3.4 | 0.031 | 1/7 (A498) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +3.3 | 0.032 | 1/6 (A-172) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.044 | 2/14 (AsPC-1, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.47×** | +3.1 | 0.057 | 0/8 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.51×** | +3.1 | 0.058 | 0/12 | inconsistent across doses | position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.059 | 0/16 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5066.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.0299×, NCI-H460 0.117×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.126×, NCI-H2030 0.206×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0970×, A549 0.0866×); [[Panobinostat (drug)]] 5 µM in 2 lines (PANC-1 0.230×, NCI-H460 0.118×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Decitabine (drug)]] 5 µM |  | 0.655× | -3.4 | 0.19 | 4/22 (A-427, LOX-IMVI, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | 0.465× | -3.3 | 0.19 | 7/20 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.684× | -3.2 | 0.19 | 9/27 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.684× | -3.2 | 0.19 | 0/26 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | 0.686× | -3.1 | 0.19 | 6/21 (NCI-H1573, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.5 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.93× (z +12.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.230× (z -9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.230× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 4.78 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0970× (z -9.9) |
| [[A549 (line)]] | wt | 8.27 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -10.5) |
| [[A498 (line)]] | wt | 1.90 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 24.7× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.62× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 9.45 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0299× (z -15.1) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 8.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -8.5) |
| [[A-172 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.710 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.709 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.914 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.720 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.937 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.764 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.728 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P4HA3]] | +0.63 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[PPEF1]] | +0.61 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[HORMAD1]] | +0.59 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[SPDYE10]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PLAC4]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[CLDN16]] | +0.55 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[AMDHD1]] | +0.54 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[SERPIND1]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[SMOC1]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[AADACL2-AS1]] | +0.52 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[SERPINB11]] | +0.52 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[DENND5B-AS1]] | +0.52 | +0.43 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELOVL2]] | B | ELOVL2 activity raises CACNG6's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 1.81× lower at baseline in the lines without ELOVL2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046 |
| [[NR2E3]] | B | NR2E3 activity raises CACNG6's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 1.60× lower at baseline in the lines without NR2E3 | 0.074 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOS1]] | B | CACNG6 activity lowers NOS1's level | lines that do not express CACNG6 (18) vs lines expressing it (32) | 1.20× higher at baseline in the lines without CACNG6 | 0.021 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, RAB31, CYP27C1 |
| [[CACNG8]] | C | CACNG6 activity raises CACNG8's level | lines that do not express CACNG6 (18) vs lines expressing it (32) | 4.06× lower at baseline in the lines without CACNG6 | 0.010 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, RAB31, CYP27C1; co-absent with the target |
| [[CYP27C1]] | C | CACNG6 activity raises CYP27C1's level | lines that do not express CACNG6 (18) vs lines expressing it (32) | 4.12× lower at baseline in the lines without CACNG6 | 0.020 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, RAB31, CYP27C1; co-absent with the target |
| [[PRRX2]] | C | CACNG6 activity raises PRRX2's level | lines that do not express CACNG6 (18) vs lines expressing it (32) | 2.57× lower at baseline in the lines without CACNG6 | 0.040 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, RAB31, CYP27C1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.2, 37.9); signed map (40.0, 42.6). **Vector** length 45.3, 8.71% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +19.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +13.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +11.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.7 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | +0.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit gamma 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:53,991,637-54,012,666 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Calcium channel auxiliary gamma subunits |
| Reactome | 4 pathways, smallest: Phase 2 - plateau phase; Phase 0 - rapid depolarisation; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXT2](https://www.uniprot.org/uniprotkb/Q9BXT2) (Voltage-dependent calcium channel gamma-6 subunit):

> Regulates the activity of L-type calcium channels that contain CACNA1C as pore-forming subunit.

**Summary**, from NCBI Gene [59285](https://www.ncbi.nlm.nih.gov/gene/59285):

> Voltage-dependent calcium channels are composed of five subunits. The protein encoded by this gene represents one of these subunits, gamma, and is one of two known gamma subunit proteins. This particular gamma subunit is an integral membrane protein that is thought to stabilize the calcium channel in an inactive (closed) state. This gene is part of a functionally diverse eight-member protein subfamily of the PMP-22/EMP/MP20 family and is located in a cluster with two family members that …

**Accessions** — [HGNC:13625](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13625) · Entrez [59285](https://www.ncbi.nlm.nih.gov/gene/59285) · UniProt [Q9BXT2](https://www.uniprot.org/uniprotkb/Q9BXT2) · Ensembl [ENSG00000130433](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130433)

## Data

Gene col 5066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5066); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5066]; `tensor/DDL_lfc|DDL_z.npy` [5066]; `embed/gene_vectors.npy` [5066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5066 or target_col == 5066). Every well: [[CACNG6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNG6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
