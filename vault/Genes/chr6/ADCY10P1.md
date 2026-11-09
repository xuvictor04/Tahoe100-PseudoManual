---
symbol: "ADCY10P1"
type: "gene"
col: 8459
ensembl_id: "ENSG00000161912"
name: "ADCY10 pseudogene 1"
location: "6p21.1"
module: 38
arm: "+"
pooled_cpm: 12.02
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ADCY10P1

*ADCY10 pseudogene 1* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.47× (z +16.1, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.343× (z -5.2, q 1e-04, down in 27 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (AsPC-1 0.0731×, H4 0.108×, NCI-H2030 0.126×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.115×, LOX-IMVI 0.125×, RPMI-7951 0.138×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change); [[Docetaxel (drug)]] 0.05 µM in 2 lines (HS-578T 0.137×, hTERT-HPNE 0.116×; ⚠ transcription drop; cell-cycle shift, explains ~66% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02936]] (+0.83, fdr 7e-06), [[FNDC7]] (+0.80, fdr 7e-06), [[PILRA]] (+0.80, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[C9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8459.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.47×** | +16.1 | 0e+00 | 41/43 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +10.4 | 1e-22 | 29/43 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +8.2 | 3e-14 | 30/44 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +6.8 | 2e-09 | 31/40 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.99×** | +6.3 | 3e-08 | 37/47 (SW1417, HepG2/C3A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +5.1 | 3e-05 | 27/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +5.0 | 4e-05 | 26/44 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +4.9 | 7e-05 | 21/42 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.6 | 3e-04 | 19/47 (SW480, SHP-77, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.9 | 0.005 | 5/47 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.053 | 17/46 (KATO III, SHP-77, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.078 | 11/47 (SW 900, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8459.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (AsPC-1 0.0731×, H4 0.108×, NCI-H2030 0.126×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.115×, LOX-IMVI 0.125×, RPMI-7951 0.138×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change); [[Docetaxel (drug)]] 0.05 µM in 2 lines (HS-578T 0.137×, hTERT-HPNE 0.116×; ⚠ transcription drop; cell-cycle shift, explains ~66% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.343×** | -5.2 | 1e-04 | 27/40 (COLO 205, H4, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.691× | -3.5 | 0.13 | 12/41 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | 0.499× | -3.4 | 0.13 | 16/41 (RPMI-7951, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.691× | -3.3 | 0.13 | 19/45 (RKO, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.713× | -3.2 | 0.17 | 20/44 (AsPC-1, H4, …) | top dose only | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 31.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +9.9) | [[Docetaxel (drug)]] 0.05 µM 0.137× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~66% of this change |
| [[LOX-IMVI (line)]] | wt | 18.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.56× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[AsPC-1 (line)]] | alt | 12.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.35× (z +13.2) | [[Digitoxin (drug)]] 5 µM 0.0731× (z -11.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 35.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 24.3 | 0 | 2 (1 ⚠) | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.101× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 18.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.126× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 3.89 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.98× (z +11.3) | [[Selinexor (drug)]] 0.5 µM 0.0437× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 4.95 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.79× (z +13.5) | — |
| [[A-172 (line)]] | wt | 4.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +10.9) | — |
| [[C32 (line)]] | wt | 7.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 42.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 8.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.94× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[NCI-H23 (line)]] | alt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 15.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +10.3) | — |
| [[RKO (line)]] | wt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 8.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.77× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +9.6) | — |
| [[SW480 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0483× (z -10.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02936]] | +0.83 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.80 | +0.81 / +0.75 | both halves | 7e-06 |  |
| [[PILRA]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.79 | +0.74 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.78 | +0.81 / +0.72 | both halves | 7e-06 |  |
| [[PYGM]] | +0.78 | +0.78 / +0.81 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.78 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[VWCE]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.76 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.76 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.76 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C9]] | B | C9 activity raises ADCY10P1's level | lines that do not express C9 (21) vs lines expressing it (29) | 1.42× lower at baseline in the lines without C9 | 0.004 | ⚠ within organs, on part of the lines; also absent: DAB2, ENSG00000253891, PTGFR |
| [[TOP2A]] | B | TOP2A activity lowers ADCY10P1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FES]] | B | FES activity raises ADCY10P1's level | lines that do not express FES (11) vs lines expressing it (39) | 1.69× lower at baseline in the lines without FES | 0.090 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.821). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.5, -16.7); signed map (14.6, 9.4). **Vector** length 98.1, 22.2% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +16.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +6.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.3 | +6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +8.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +2.4 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | +3.3 |
|  | [[NG25 (drug)]] 5 µM |  | -3.4 | -5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | +1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.1 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ADCY10 pseudogene 1 |
| Locus type | pseudogene |
| Location | 6p21.1 — chr6:41,101,022-41,138,727 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44143) · Entrez [221442](https://www.ncbi.nlm.nih.gov/gene/221442) · Ensembl [ENSG00000161912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161912)

## Data

Gene col 8459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8459); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8459]; `tensor/DDL_lfc|DDL_z.npy` [8459]; `embed/gene_vectors.npy` [8459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8459 or target_col == 8459). Every well: [[ADCY10P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADCY10P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
