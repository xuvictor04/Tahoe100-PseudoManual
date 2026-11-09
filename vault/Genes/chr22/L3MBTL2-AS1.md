---
symbol: "L3MBTL2-AS1"
type: "gene"
col: 14023
ensembl_id: "ENSG00000235513"
name: "L3MBTL2 antisense RNA 1"
location: "22q13.2"
module: 53
arm: "+"
pooled_cpm: 3.41
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# L3MBTL2-AS1

*L3MBTL2 antisense RNA 1* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.19× (z +21.7, q 0e+00, up in 29 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.553× (z -5.5, q 2e-05, down in 22 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Nimesulide (drug)]] 5 µM in 1 line (SW480 0.0879×; ⚠ toxic; unreliable plate only); [[Erlotinib (drug)]] 5 µM in 1 line (LoVo 0.0562×); [[Vilanterol (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0729×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00393]] (+0.81, fdr 7e-06), [[USP50]] (+0.80, fdr 7e-06), [[CHADL]] (+0.80, fdr 7e-06, ⚠ same locus), [[DNAH10]] (+0.79, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14023.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.19×** | +21.7 | 0e+00 | 29/35 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.73×** | +20.5 | 0e+00 | 35/36 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.54×** | +8.7 | 5e-16 | 19/34 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +8.7 | 5e-16 | 28/44 (SW480, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +8.1 | 7e-14 | 21/34 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +7.0 | 3e-10 | 2/3 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +6.3 | 2e-08 | 4/16 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +6.1 | 6e-08 | 21/45 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +6.1 | 6e-08 | 19/37 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.3 | 7e-06 | 6/20 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.2 | 1e-05 | 15/45 (A498, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +4.4 | 6e-04 | 7/44 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.006 | 8/44 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +3.6 | 0.012 | 7/42 (LoVo, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.2 | 0.047 | 1/8 (A498) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.054 | 3/31 (SW480, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.054 | 11/44 (CFPAC-1, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14023.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Nimesulide (drug)]] 5 µM in 1 line (SW480 0.0879×; ⚠ toxic; unreliable plate only); [[Erlotinib (drug)]] 5 µM in 1 line (LoVo 0.0562×); [[Vilanterol (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0729×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.553×** | -5.5 | 2e-05 | 22/43 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM |  | 0.774× | -3.4 | 0.19 | 8/45 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 5 µM |  | 0.709× | -3.2 | 0.22 | 9/45 (RPMI-7951, NCI-H2347, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.788× | -3.2 | 0.22 | 10/44 (AsPC-1, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 3.91 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.59× (z +11.1) | [[Vilanterol (drug)]] 0.5 µM 0.0729× (z -9.1) |
| [[LoVo (line)]] | wt | 3.79 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +13.4) | [[Erlotinib (drug)]] 5 µM 0.0562× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 3.19 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 2.16 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +11.5) | — |
| [[SW480 (line)]] | alt | 2.53 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.27× (z +10.9) | [[Nimesulide (drug)]] 5 µM 0.0879× (z -9.5) ⚠ toxic; unreliable plate only |
| [[C32 (line)]] | wt | 3.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +12.2) | — |
| [[HCT15 (line)]] | alt | 4.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 1.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.2× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 2.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 2.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.5× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 3.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 2.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 3.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.18× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 1.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 3.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.12× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 1.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +9.8) | — |
| [[A-172 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00393]] | +0.81 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[USP50]] | +0.80 | +0.87 / +0.60 | both halves | 7e-06 |  |
| [[CHADL]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 | ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[DNAH10]] | +0.79 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[PEBP4]] | +0.79 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.77 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[MPP4]] | +0.77 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[SGSM3-AS1]] | +0.77 | +0.84 / +0.61 | both halves | 7e-06 | same gene group |
| [[MYOCOS]] | +0.77 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[MFSD2B]] | +0.77 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[DPYS]] | +0.76 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[SLC4A10]] | +0.76 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[AXDND1]] | +0.76 | +0.77 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers L3MBTL2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[F2]] | B | F2 activity raises L3MBTL2-AS1's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.28× lower at baseline in the lines without F2 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SCUBE2]] | B | SCUBE2 activity strengthens L3MBTL2-AS1's drug response | lines that do not express SCUBE2 (7) vs lines expressing it (38) | the lines without SCUBE2 respond 0.93× as strongly (z diff +0.31); strongest at Dinaciclib 0.5 µM: 0.47x vs 1.82x (z diff +4.4) | 0.093 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.1, -13.7); signed map (20.8, 9.9). **Vector** length 67.2, 10.1% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +21.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +20.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | L3MBTL2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q13.2 — chr22:41,207,592-41,228,500 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40847) · Entrez [100506544](https://www.ncbi.nlm.nih.gov/gene/100506544) · Ensembl [ENSG00000235513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235513)

## Data

Gene col 14023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14023); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14023]; `tensor/DDL_lfc|DDL_z.npy` [14023]; `embed/gene_vectors.npy` [14023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14023 or target_col == 14023). Every well: [[L3MBTL2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/L3MBTL2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
